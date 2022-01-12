from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework.response import Response
from django.utils import timezone

from .models import Question, Survey, Choice, Answer
from .serializers import SurveySerializer, QuestionSerializer, ChoiceSerializer, AnswerSerializer


@api_view(["GET"])
def login(request):
    """
        User authentication function
    """

    # get details from the request
    username = request.data.get("username")
    password = request.data.get("password")

    if username is None or password is None:
        return Response({'error': 'Authentication Error'},
                        status=status.HTTP_401_UNAUTHORIZED)

    # Authenticating the user
    user = authenticate(username=username, password=password)

    # Wrong details
    if not user:
        return Response({'error': 'Authentication Error'},
                        status=status.HTTP_401_UNAUTHORIZED)

    # creating token for the user
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=status.HTTP_200_OK)

@api_view(["GET"])
def register(request):
    """
        User registration
    """

    username = request.data.get("username")
    password = request.data.get("password")

    if username is None:
        return Response({'error': 'Invalid username'})

    if password is None:
        return Response({'error': 'Invalid password'})

    # creating user with empty password
    user = User.objects.create_user(username, '', password)

    # creating token for the user
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((IsAuthenticated, IsAdminUser,))
def survey_create(request):
    """
        Creating survey based on user input
    """
    serializer = SurveySerializer(data=request.data, context={'request': request})

    # survey validation
    if serializer.is_valid():
        survey = serializer.save()
        return Response(SurveySerializer(survey).data, status=status.HTTP_201_CREATED)

    # survey is not valid
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH', 'DELETE'])
@permission_classes((IsAuthenticated, IsAdminUser,))
def survey_update(request, survey_id):
    """
        Updating existing survey
    """
    survey = get_object_or_404(Survey, pk=survey_id)

    # update survey
    if request.method == 'PATCH':
        serializer = SurveySerializer(survey, data=request.data, partial=True)
        if serializer.is_valid():
            survey = serializer.save()
            return Response(SurveySerializer(survey).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete survey
    elif request.method == 'DELETE':
        survey.delete()
        return Response("Survey Successfully deleted", status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def survey_view(request):
    """
        Get list of all the surveys
    """
    survey = Survey.objects.all()
    serializer = SurveySerializer(survey, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes((IsAuthenticated, IsAdminUser,))
def question_create(request):
    """
        Create a question based on user input
    """
    serializer = QuestionSerializer(data=request.data)

    # validating input
    if serializer.is_valid():
        question = serializer.save()
        return Response(QuestionSerializer(question).data, status=status.HTTP_201_CREATED)

    # invalid input
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH', 'DELETE'])
@permission_classes((IsAuthenticated, IsAdminUser,))
def question_update(request, question_id):
    """
        updating or deleting existing question
    """
    question = get_object_or_404(Question, pk=question_id)

    # update question
    if request.method == 'PATCH':
        serializer = QuestionSerializer(question, data=request.data, partial=True)

        # question data validation
        if serializer.is_valid():
            question = serializer.save()
            return Response(QuestionSerializer(question).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete question
    elif request.method == 'DELETE':
        question.delete()
        return Response("Question deleted", status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((IsAuthenticated, IsAdminUser,))
def choice_create(request):
    """
        Creating a choice
    """
    serializer = ChoiceSerializer(data=request.data)

    # choice input validating
    if serializer.is_valid():
        choice = serializer.save()
        return Response(ChoiceSerializer(choice).data, status=status.HTTP_201_CREATED)

    # wrong input
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH', 'DELETE'])
@permission_classes((IsAuthenticated, IsAdminUser,))
def choice_update(request, choice_id):
    """
        Updating or Deleting a choice
    """
    choice = get_object_or_404(Choice, pk=choice_id)

    # updating
    if request.method == 'PATCH':
        serializer = ChoiceSerializer(choice, data=request.data, partial=True)

        # input validation
        if serializer.is_valid():
            choice = serializer.save()
            return Response(ChoiceSerializer(choice).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # deleting
    elif request.method == 'DELETE':
        choice.delete()
        return Response("choice has been deleted.", status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_active_surveys(request):
    """
        get active surveys list
    """
    survey = Survey.objects.filter(end_date__gte=timezone.now()).filter(public_date__lte=timezone.now())
    serializer = SurveySerializer(survey, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def answer_create(request):
    """
        Create user answer
    """
    serializer = AnswerSerializer(data=request.data, context={'request': request})

    # input validation
    if serializer.is_valid():
        answer = serializer.save()
        return Response(AnswerSerializer(answer).data, status=status.HTTP_201_CREATED)

    # invalid input
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_answer(request, user_id):
    """
        Getting answers list
    """
    answers = Answer.objects.filter(user_id=user_id)
    serializer = AnswerSerializer(answers, many=True)
    return Response(serializer.data)


@api_view(['PATCH', 'DELETE'])
@permission_classes((IsAuthenticated, IsAdminUser,))
def answer_update(request, answer_id):
    """
        Updating user answer
    """
    answer = get_object_or_404(Answer, pk=answer_id)

    # update based on user input
    if request.method == 'PATCH':
        serializer = AnswerSerializer(answer, data=request.data, partial=True)
        if serializer.is_valid():
            answer = serializer.save()
            return Response(AnswerSerializer(answer).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete answer
    elif request.method == 'DELETE':
        answer.delete()
        return Response("Answer has been deleted", status=status.HTTP_204_NO_CONTENT)
