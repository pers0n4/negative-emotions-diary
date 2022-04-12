from typing import Optional

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


# https://datatracker.ietf.org/doc/html/rfc7519#section-4
class JwtRegisteredClaim(BaseModel):
    iss: Optional[str] = None
    sub: Optional[str] = None
    aud: Optional[str] = None
    exp: Optional[int] = None
    nbf: Optional[int] = None
    iat: Optional[int] = None
    jti: Optional[str] = None
