from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bbs.models import Bbs
from bbs.serializers import BbsSerializer


@api_view(['GET', 'POST'])
def bbs_list(request, format=None):
    if request.method == 'GET':  # GET 으로 요청 시
        bbs = Bbs.objects.all()
        serializer = BbsSerializer(bbs, many=True)  # 시리얼라이저를 거쳐 json로 변경 된 데이터를 응답
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BbsSerializer(data=request.data)  # 요청한 data를 Serializer로 전달
        if serializer.is_valid():  # 검증
            serializer.save()  # 검증이 문제가 없다면 save
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])  # detail pk 로 접근 가능
def bbs_detail(request, pk, format=None):
    try:
        bbs = Bbs.objects.get(pk=pk)  # 접근한 pk에 맞는 인스턴스가 있다면 bbs에 저장
    except Bbs.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)  # 접근을 잘못한 사람이 있다면 404

    if request.method == 'GET':  # GET으로 요청했다는 것은 데이터를 얻어가고 싶다는 것이기 때문에
        serializer = BbsSerializer(bbs)
        return Response(serializer.data)  # 직렬화 된 데이터를 응답해준다.

    elif request.method == 'PUT':  # PUT과 PATCH의 차이에 대해 알 필요가 있다. PUT은 전체 업데이트
        serializer = BbsSerializer(bbs, data=request.data)  # PUT 업데이트해달라는 데이터가 있을 것
        if serializer.is_valid():  # 검증
            serializer.save()  # 저장
            return Response(serializer.data)  # 응답
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # 잘못 된 요청이면 400

    elif request.method == 'DELETE':  # 삭제 요청 시
        bbs.delete()  # pk 에 맞는 obj 를 삭제
        return Response(status=status.HTTP_204_NO_CONTENT)
