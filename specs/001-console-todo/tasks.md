# Tasks: Console Todo App

**Input**: Design documents from `/specs/001-console-todo/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure per implementation plan in root directory
- [x] T002 Create src/ directory for Python source code
- [x] T003 [P] Create README.md with setup and run instructions
- [x] T004 [P] Create QWEN.md with prompt templates and instructions for using Qwen
- [x] T005 Create .gitignore file with appropriate Python ignores

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T006 [P] Create Task dataclass in src/models/task.py based on data model requirements
- [x] T007 Create TaskManager class in src/task_manager.py with in-memory storage implementation
- [x] T008 Implement TaskManager.add_task() method with auto-incrementing ID generation
- [x] T009 Implement TaskManager.get_all_tasks() method
- [x] T010 Implement TaskManager.get_task_by_id() method
- [x] T011 Implement TaskManager.update_task() method
- [x] T012 Implement TaskManager.delete_task() method
- [x] T013 Implement TaskManager.toggle_task_completion() method
- [x] T014 Create validation functions for input validation in src/utils/validation.py
- [x] T015 Create constants for application configuration in src/config.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Tasks (Priority: P1) 🎯 MVP

**Goal**: Implement the ability to add new tasks to the todo list with required title and optional description

**Independent Test**: Can be fully tested by adding multiple tasks with different titles and descriptions, verifying they appear in the task list with correct IDs and completion status.

### Implementation for User Story 1

- [x] T016 Create main.py with basic application structure and menu loop
- [x] T017 Implement display_menu() function to show menu options
- [x] T018 Implement handle_add_task() function to prompt for title/description and add to TaskManager
- [x] T019 Add menu option 1 for adding tasks in the main loop
- [x] T020 Implement input validation for task title (non-empty, max 200 chars)
- [x] T021 Test adding tasks with valid titles and descriptions
- [x] T022 Test adding tasks with empty descriptions (optional field)

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

**Goal**: Implement the ability to view all tasks with their ID, title, description, and completion status ([ ] or [x])

**Independent Test**: Can be fully tested by adding multiple tasks and verifying they all appear correctly in the list with proper formatting and status indicators.

### Implementation for User Story 2

- [x] T023 Implement handle_view_tasks() function to display all tasks with proper formatting
- [x] T024 Add menu option 2 for viewing tasks in the main loop
- [x] T025 Implement proper display formatting with ID, title, description, and [ ]/[x] indicators
- [x] T026 Handle empty task list case with appropriate message
- [x] T027 Test viewing tasks after adding them via User Story 1

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Tasks as Complete/Incomplete (Priority: P1)

**Goal**: Implement the ability to mark tasks as complete or incomplete by toggling their status

**Independent Test**: Can be fully tested by adding tasks, marking them as complete/incomplete, and verifying the status changes are reflected when viewing the task list.

### Implementation for User Story 3

- [x] T028 Implement handle_mark_task() function to toggle completion status
- [x] T029 Add menu option 5 for marking tasks as complete/incomplete in the main loop
- [x] T030 Implement validation for task ID input (must exist)
- [x] T031 Test toggling completion status of tasks
- [x] T032 Test error handling for non-existent task IDs

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Update Task Details (Priority: P2)

**Goal**: Implement the ability to update the details of existing tasks by ID

**Independent Test**: Can be fully tested by adding tasks, updating their details, and verifying the changes are reflected when viewing the task list.

### Implementation for User Story 4

- [x] T033 Implement handle_update_task() function to update title/description by ID
- [x] T034 Add menu option 3 for updating tasks in the main loop
- [x] T035 Implement validation for update inputs (title must be non-empty if provided)
- [x] T036 Test updating task titles and descriptions
- [x] T037 Test error handling for non-existent task IDs

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Delete Tasks (Priority: P2)

**Goal**: Implement the ability to delete tasks by ID

**Independent Test**: Can be fully tested by adding tasks, deleting some of them, and verifying the remaining tasks are still accessible and the deleted ones are gone.

### Implementation for User Story 5

- [x] T038 Implement handle_delete_task() function to remove tasks by ID
- [x] T039 Add menu option 4 for deleting tasks in the main loop
- [x] T040 Implement confirmation prompt for task deletion
- [x] T041 Test deleting tasks and verifying they're removed
- [x] T042 Test error handling for non-existent task IDs

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T043 Implement graceful exit functionality for menu option 6
- [x] T044 Add comprehensive error handling for all user inputs
- [x] T045 Implement validation for all user inputs (numeric IDs, non-empty titles, etc.)
- [x] T046 [P] Add comments and docstrings to all functions and classes
- [x] T047 Ensure PEP 8 compliance across all Python files
- [x] T048 Test all menu options and error handling scenarios
- [x] T049 Run quickstart.md validation to ensure application works as expected

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 5 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable

### Within Each User Story

- Models before services
- Services before UI implementation
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all models for User Story 1 together:
Task: "Create Task dataclass in src/models/task.py based on data model requirements"
Task: "Create validation functions for input validation in src/utils/validation.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence