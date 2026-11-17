from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path

ROOT = Path(__file__).parent / "workdir"


AGENTS_MD = """# AGENTS.md

This repo runs with a workbench. Read these before acting:

1. `agent_state.json`: where the last session stopped.
2. `task_board.json`: what is in flight, what is next.
3. `docs/agent-rules.md`: startup, scope, definition of done (load on demand).

Definition of done: the task referenced by `agent_state.active_task_id` has
`status == "done"` on `task_board.json` and the verification command listed in
its `acceptance` has exited 0.

Verification command: `python3 -m pytest -x`
""".lstrip()


@dataclass
class AgentState:
    active_task_id: str | None
    touched_files: list[str] = field(default_factory=list)
    assumptions: list[str] = field(default_factory=list)
    blockers: list[str] = field(default_factory=list)
    next_action: str = ""
    lastrun : int = 0


@dataclass
class Task:
    id: str
    goal: str
    owner: str
    acceptance: list[str]
    status: str = "todo"
    priority: int = 0


def write_initial(state_path: Path, board_path: Path, agents_path: Path) -> None:
    if not agents_path.exists():
        agents_path.write_text(AGENTS_MD)
    if not state_path.exists():
        state_path.write_text(json.dumps(asdict(AgentState(active_task_id=None)), indent=2) + "\n")
    if not board_path.exists():
        board = [
            Task(
                id="T-001",
                goal="add input validation to /signup",
                owner="builder",
                acceptance=["pytest test_app.py::test_signup_rejects_short_password"],
                priority=2
            ),
        ]
        board_path.write_text(json.dumps([asdict(t) for t in board], indent=2) + "\n")


def load_state(state_path: Path) -> AgentState:
    raw = json.loads(state_path.read_text())
    return AgentState(**raw)


def load_board(board_path: Path) -> list[Task]:
    return [Task(**t) for t in json.loads(board_path.read_text())]


def save_state(state_path: Path, state: AgentState) -> None:
    state_path.write_text(json.dumps(asdict(state), indent=2) + "\n")


def save_board(board_path: Path, board: list[Task]) -> None:
    board_path.write_text(json.dumps([asdict(t) for t in board], indent=2) + "\n")



def make_files() -> None:
    ROOT.mkdir(exist_ok=True)
    state_path = ROOT / "agent_state.json"
    board_path = ROOT / "task_board.json"
    agents_path = ROOT / "AGENTS.md"

    write_initial(state_path, board_path, agents_path)
    # state = load_state(state_path)
    # board = load_board(board_path)

    # print("before turn:")
    # print(f"  active task : {state.active_task_id}")
    # print(f"  next action : {state.next_action!r}")
    # print(f"  todo on board: {[t.id for t in board if t.status == 'todo']}")

    # state, board = run_one_turn(state, board)
    # save_state(state_path, state)
    # save_board(board_path, board)

    # print("\nafter turn:")
    # print(f"  active task : {state.active_task_id}")
    # print(f"  touched     : {state.touched_files}")
    # print(f"  next action : {state.next_action!r}")
    # print(f"  board status: {[(t.id, t.status) for t in board]}")

