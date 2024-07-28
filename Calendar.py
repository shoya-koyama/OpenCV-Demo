from google.oauth2 import service_account
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import os

# 設定
KEYPASS = '***'
TOKENDIRPASS = '***'
CALID = '***.com'
CALIDHOLIDAY = 'ja.japanese#holiday@group.v.calendar.google.com'

# 認証情報を読み込む
credentials = service_account.Credentials.from_service_account_file(KEYPASS)

# トークンディレクトリが存在しない場合は作成する
if not os.path.exists(TOKENDIRPASS):
    os.makedirs(TOKENDIRPASS)

token_path = os.path.join(TOKENDIRPASS, 'token.json')

# トークンファイルを読み込み、必要に応じて更新する
if os.path.exists(token_path):
    credentials.token = open(token_path, 'r').read()
else:
    # 必要に応じて認証フローを実行し、トークンを取得する
    credentials.refresh(Request())
    with open(token_path, 'w') as token_file:
        token_file.write(credentials.token)

print("認証が完了しました。")

# Google Calendar APIのサービスオブジェクトを作成
service = build('calendar', 'v3', credentials=credentials)

# 作業報告書テンプレートのイベント作成
event = {
    'summary': 'バイト',
    'location': '',
    'description': 'バイトについて.',
    'start': {
        'dateTime': '20**-**-**T**:00:00+09:00',
        'timeZone': 'Asia/Tokyo',
    },
    'end': {
        'dateTime': '20**-**-**T**:00:00+09:00',
        'timeZone': 'Asia/Tokyo',
    },
    'recurrence': [
        'RRULE:FREQ=WEEKLY;BYDAY=**'  # 毎週月曜日に繰り返し
    ],
    'reminders': {
        'useDefault': False,
        'overrides': [
            {'method': 'email', 'minutes': 24 * 60},  # 1日前にメール通知
            {'method': 'popup', 'minutes': 10},       # 10分前にポップアップ通知
        ],
    },
}

# イベントをカレンダーに挿入
event_result = service.events().insert(calendarId=CALID, body=event).execute()
print(f"Created Event ID: {event_result['id']}")
print(f"Summary: {event_result['summary']}")
print(f"Description: {event_result['description']}")
print(f"Start: {event_result['start']['dateTime']}")
print(f"End: {event_result['end']['dateTime']}")
print(f"TimeZone: {event_result['start']['timeZone']}")
print(f"Recurrence: {event_result.get('recurrence', 'None')}")
print(f"Reminders: {event_result.get('reminders', 'None')}")