@app.post("/refresh")
def refresh_token(token: str = Depends(oauth2_scheme)):
    payload = verify_jwt(token)

    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired refresh Token")
    
    # generate_new_access_token
    new_access_token = create_jwt({"sub":payload["sub"]})

    return {"access_token":new_access_token,"token_type":"bearer"}