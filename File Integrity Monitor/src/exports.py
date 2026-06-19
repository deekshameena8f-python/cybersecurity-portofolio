import csv
from datetime import datetime


def export_to_csv(changes):
    """
    Export detected changes to CSV.
    """

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"data/reports/report_{timestamp}.csv"

    with open(filename, "w", newline="") as csvfile:

        writer = csv.writer(csvfile)

        writer.writerow(["Change Type", "File"])

        for file in changes["modified"]:
            writer.writerow(["Modified", file])

        for file in changes["new"]:
            writer.writerow(["New", file])

        for file in changes["deleted"]:
            writer.writerow(["Deleted", file])

    return filename
