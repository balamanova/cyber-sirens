cognitive_tests = [
     {"id": 1, "phq_9": "phq_9", "description": "This test is a multipurpose instrument for screening, diagnosing, monitoring and measuring the severity of person's depression "},
     {"id": 2, "gad_7": "gad_7", "description": "This test is a seven-item instrument that is used to measure or assess the severity of generalised anxiety disorder (GAD)"},
     {"id": 3, "pss": "pss", "description": "This test is a classic stress assessment instrument, that is used to understand how different situations affect person's feelings and person's perceived stress."}
 ]

# class CognitiveTestResult(BaseModel):
#     test_id: int
#     user_id: int
#     score: int
    

# @app.get("/tests", response_model=List[dict])
# async def get_tests():
#     return cognitive_tests


# @app.get("/tests/{id}", response_model=dict)
# async def get_test(id: int):
#     test = next((test for test in cognitive_tests if test["id"] == id), None)
#     if test is None:
#         raise HTTPException(status_code=404, detail="Test not found")
#     return test


# @app.post("/submit")
# async def submit_result(result: CognitiveTestResult):
#     print(f"Saved test result: {result}")
    
#     result_message = "less stress" if result.score < 50 else "high stress"
#     return {"message": "Success", "result": result_message}
