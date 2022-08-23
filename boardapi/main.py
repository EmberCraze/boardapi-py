from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class TicTacToe(BaseModel):
    # An array of moves for each player
    moves_player_one: list[list[int]] = Field(default=[[]])
    moves_player_two: list[list[int]] = Field(default=[[]])
    turn: int = Field(default=1)


tictactoes = TicTacToe()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/tictactoe")
async def tic_tac_toe(tictactoe: TicTacToe):
    tictactoes = tictactoe
    return tictactoes


@app.get("/tictactoe")
async def tic_tac_toe():
    return tictactoes
