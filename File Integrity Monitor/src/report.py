from datetime import datetime


def generate_report(
    modified,
    new_files,
    deleted
):

    report_name = (
        f"data/reports/"
        f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    )

    with open(report_name, "w") as report:

        report.write(
            "FILE INTEGRITY REPORT\n"
        )

        report.write(
            "=" * 40 + "\n\n"
        )

        report.write(
            f"Modified Files:\n{modified}\n\n"
        )

        report.write(
            f"New Files:\n{new_files}\n\n"
        )

        report.write(
            f"Deleted Files:\n{deleted}\n"
        )
