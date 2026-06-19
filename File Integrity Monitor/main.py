import time

from src.baseline import load_baseline
from src.monitor import detect_changes
from src.report import generate_report
from src.alerts import display_alerts, send_email_alert
from src.export import export_to_csv


TARGET_DIRECTORY = "."
ENABLE_EMAIL_ALERTS = False


def main():
    """
    Main File Integrity Monitoring workflow.
    """
    print("File Integrity Monitor Started...")


    baseline_data = load_baseline()
    while True:
        changes = detect_changes(
            TARGET_DIRECTORY,
            baseline_data
        )
        
        if any(changes.values()):
            print("\nChanges Detected!\n")

            # Generate text report
            generate_report(changes)

            # Generate CSV report
            export_to_csv(changes)

            # Show colored console alerts
            display_alerts(changes)

            # Send email notification
             if ENABLE_EMAIL_ALERTS:
                send_email_alert(changes)
        
        else:
            print("No changes detected.")

        time.sleep(60)


if __name__ == "__main__":
    main()
