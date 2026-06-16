from tabulate import tabulate


def display_records(attendance_book):
    """
    Hiển thị bảng chấm công.
    """

    if not attendance_book:
        print("Chưa có dữ liệu chấm công.")
        return

    table_data = []

    for employee in attendance_book:

        clock_in, clock_out = employee["times"]

        if clock_out is None:
            clock_out = "[Đang làm việc]"

        table_data.append([
            employee["id"],
            employee["name"],
            clock_in,
            clock_out
        ])

    print("\n--- BẢNG CHẤM CÔNG ---")

    print(
        tabulate(
            table_data,
            headers=[
                "Mã NV",
                "Tên Nhân Viên",
                "Giờ Vào",
                "Giờ Ra"
            ],
            tablefmt="grid"
        )
    )