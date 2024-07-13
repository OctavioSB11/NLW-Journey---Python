import uuid
import pytest 
from .participants_repository import ParticipantsRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
participant_id = str(uuid.uuid4())
trip_id = str(uuid.uuid4())
emails_to_invite_id = str(uuid.uuid4())

#Tests de integracao entre DB e programa

#@pytest.mark.skip(reason="interacao com o banco") #faz com que teste mas nao atualiza o banco toda hr
def test_create_participant():
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)

    participant_infos = {
        "id": participant_id,
        "trip_id": trip_id,
        "emails_to_invite_id": emails_to_invite_id,
        "name": "jonas silva" 
    }

    participants_repository.registry_participant(participant_infos)

@pytest.mark.skip(reason="interacao com o banco")
def test_find_participant_by_id():
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)

    participant = participants_repository.find_participant_by_id(participant_id)
    print(participant)

@pytest.mark.skip(reason="interacao com o banco") 
def test_update_participant_status():
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)

    participants_repository.update_participant_status(participant_id)
