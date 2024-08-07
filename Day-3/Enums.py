from enum import Enum, StrEnum, auto

class HTTPStatus(Enum):
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NO_CONTENT = 204
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500
    NOT_IMPLEMENTED = 501

class RESTMethod(StrEnum):
    GET = "GET"  # auto()
    POST = "POST"  # auto()
    PUT = "PUT"  # auto()
    DELETE = "DELETE"  # auto()


for status in HTTPStatus:
    print(f"{status.name}: {status.value}")

print(f"Name of the enum member: {HTTPStatus.OK.name}")
print(f"Enum member from value: {HTTPStatus(404)}")
print(f"Value of the enum member: {HTTPStatus.NOT_FOUND.value}")

def response_description(status: HTTPStatus) -> str:
    if status == HTTPStatus.OK:
        return "Request succeeded"
    elif status == HTTPStatus.NOT_FOUND:
        return "Resource not found"
    else:
        return "Error occurred"

def main() -> None:
    status = HTTPStatus(200)
    print(response_description(status))

if __name__ == "__main__":
    main()
