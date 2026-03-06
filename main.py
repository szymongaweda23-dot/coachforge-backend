from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Optional

app = FastAPI(title="CoachForge AI Backend")

# --- DEFINICJE DANYCH (Wymuszają na AI zwracanie poprawnego formatu) ---

class UserProfile(BaseModel):
    age: int
    gender: str
    goal: str

class CoachResponse(BaseModel):
    summary: str
    next_best_actions: List[str]
    risk_flags: List[Dict[str, str]]

class TrainingSet(BaseModel):
    target_reps: str
    tempo: str
    rest_s: str
    target_rpe: str
    suggested_load: Optional[str]

class Exercise(BaseModel):
    name: str
    sets: List[TrainingSet]
    technique_cues: List[str]

class DailyPlan(BaseModel):
    day: str
    title: str
    exercises: List[Exercise]
    estimated_minutes: int

class TrainingPlanResponse(BaseModel):
    week_plan: List[DailyPlan]
    notes: List[str]

# --- ENDPOINTY (Miejsca, do których łączy się Twoja aplikacja w telefonie/przeglądarce) ---

@app.get("/")
def read_root():
    return {"status": "Serwer CoachForge AI działa poprawnie!"}

@app.post("/coach", response_model=CoachResponse)
def coach_master_endpoint(profile: UserProfile):
    # Tutaj w przyszłości połączymy się z prawdziwym OpenAI API
    # Na razie zwracamy bezpieczną atrapę (mock)
    return CoachResponse(
        summary="Zrozumiałem Twój cel. Zaczynamy pracę nad planem.",
        next_best_actions=["Zrób testowy trening", "Podepnij zegarek"],
        risk_flags=[]
    )

@app.post("/training", response_model=TrainingPlanResponse)
def training_engine_endpoint(profile: UserProfile):
    # Atrapa planu treningowego dla UI
    return TrainingPlanResponse(
        week_plan=[
            DailyPlan(
                day="2024-11-01",
                title="Trening Siłowy Górnych Partii",
                exercises=[],
                estimated_minutes=45
            )
        ],
        notes=["Pamiętaj o nawodnieniu"]
    )
