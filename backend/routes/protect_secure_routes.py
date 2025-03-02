@app.get("/protected")
def protected_route(token: str = Depends(oauth2_scheme)):
    payload = verify_jwt(token)

    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")

    return {"message": "You have access to this protected resource!"}
