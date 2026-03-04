from app.repository import create_task
from app.github_service import create_github_issue

def create_task_service(task):
    task_dict = task.dict()

    issue_id = create_github_issue(
        task_dict["title"],
        task_dict["description"]
    )

    task_dict["external_reference_id"] = issue_id

    task_id = create_task(task_dict)

    return task_id

from app.repository import get_all_tasks

# def get_tasks_service():
#     return get_all_tasks()

def get_tasks_service(page, limit):
    skip = (page - 1) * limit
    return get_all_tasks(skip, limit)

from app.repository import get_task_by_id

def get_task_service(task_id):
    return get_task_by_id(task_id)

from app.repository import update_task

# def update_task_service(task_id, task):
#     task_dict = task.dict()
#     return update_task(task_id, task_dict)

from app.github_service import update_github_issue

def update_task_service(task_id, task):

    existing_task = get_task_by_id(task_id)

    if not existing_task:
        return False

    task_dict = task.dict()

    # preserve fields that should not change
    task_dict["external_reference_id"] = existing_task.get("external_reference_id")
    task_dict["created_at"] = existing_task.get("created_at")

    update_task(task_id, task_dict)

    issue_id = existing_task.get("external_reference_id")

    if issue_id:
        update_github_issue(
            issue_id,
            task_dict["title"],
            task_dict["description"]
        )

    return True

from app.repository import delete_task

# def delete_task_service(task_id):
#     return delete_task(task_id)

from app.github_service import close_github_issue

def delete_task_service(task_id):

    existing_task = get_task_by_id(task_id)

    if not existing_task:
        return False

    issue_id = existing_task.get("external_reference_id")

    delete_task(task_id)

    if issue_id:
        close_github_issue(issue_id)

    return True

from app.repository import complete_task

def complete_task_service(task_id):
    return complete_task(task_id)