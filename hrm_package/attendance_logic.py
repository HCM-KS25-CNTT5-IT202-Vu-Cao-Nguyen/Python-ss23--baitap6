def clock_in(attendance_book):
    """
    Chấm công vào.
    """

    employee_id = input(
        "Nhập mã nhân viên: "
    ).strip().upper()

    for employee in attendance_book:

        if employee["id"] == employee_id:

            print("Mã nhân viên đã tồn tại!")
            return

    employee_name = input(
        "Nhập tên nhân viên: "
    ).strip()

    clock_in_time = input(
        "Nhập giờ vào (HH:MM): "
    ).strip()

    attendance_book.append(
        {
            "id": employee_id,
            "name": employee_name,
            "times": (
                clock_in_time,
                None
            )
        }
    )

    print(
        f"Thành công: Đã ghi nhận "
        f"{employee_id} chấm công vào lúc "
        f"{clock_in_time}!"
    )


def clock_out(attendance_book):
    """
    Chấm công ra.
    """

    employee_id = input(
        "Nhập mã nhân viên: "
    ).strip().upper()

    for employee in attendance_book:

        if employee["id"] == employee_id:

            old_clock_in = employee["times"][0]

            clock_out_time = input(
                "Nhập giờ ra (HH:MM): "
            ).strip()

            # Ghi đè tuple mới
            employee["times"] = (
                old_clock_in,
                clock_out_time
            )

            print(
                f"Đã ghi nhận giờ ra cho "
                f"{employee_id}"
            )

            return

    print("Không tìm thấy nhân viên!")