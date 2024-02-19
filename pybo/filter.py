# Created by user at 2024-02-19

def formatDateTime(value,fmt='%Y년 %m월 %d일 %p %I:%M'):
    '''
    %Y :년도
    %m :월
    %d :일
    %p : AM/PM
    %I : 시간(0~12)
    %M : 분
    :param value: 날짜와 시간
    :param fmt: 포맷
    :return: 포맷이 적용된 문자
    '''
    return value.strftime(fmt)