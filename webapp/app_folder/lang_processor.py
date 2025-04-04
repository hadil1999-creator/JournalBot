import os
from google.cloud import language_v1
from google.cloud import language_v1


credential_path = "/Users/karthikbalakrishnan/Desktop/natlangex-ed8ec355d798.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path


def sample_analyze_sentiment(text_content):

    client = language_v1.LanguageServiceClient()
    type_ = language_v1.Document.Type.PLAIN_TEXT
    language = "en"
    document = {"content": text_content, "type": type_, "language": language}
    encoding_type = language_v1.EncodingType.UTF8
    response = client.analyze_sentiment(document, encoding_type=encoding_type)
    return response


def sample_analyze_syntax(text_content):

    client = language_v1.LanguageServiceClient()
    type_ = language_v1.Document.Type.PLAIN_TEXT
    language = "en"
    document = {"content": text_content, "type": type_, "language": language}
    encoding_type = language_v1.EncodingType.UTF8
    response = client.analyze_syntax(document, encoding_type=encoding_type)
    return response
