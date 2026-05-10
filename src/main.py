from task_manager import (
    get_all_tasks,
    add_task,
    update_task_status,
    delete_task,
    search_task_by_assignee
)


def main():
    tasks = []

    tasks = add_task(
        tasks,
        "Membuat CI Pipeline",
        "Menambahkan GitHub Actions untuk automated testing",
        "high",
        "Saya"
    )

    print("Daftar Task:")
    print(get_all_tasks(tasks))

    tasks = update_task_status(tasks, 1, "done")
    print("Setelah update status:")
    print(get_all_tasks(tasks))

    result = search_task_by_assignee(tasks, "saya")
    print("Hasil pencarian berdasarkan assignee:")
    print(result)

    tasks = delete_task(tasks, 1)
    print("Setelah task dihapus:")
    print(get_all_tasks(tasks))


if __name__ == "__main__":
    main()