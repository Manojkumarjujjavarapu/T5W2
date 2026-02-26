import pandas as pd
import json
import os


class ReportService:

    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path

    def load_data(self):
        try:
            students_file = os.path.join(self.input_path, "students.csv")
            attendance_file = os.path.join(self.input_path, "attendance.csv")

            students = pd.read_csv(students_file)
            attendance = pd.read_csv(attendance_file)

            return students, attendance

        except FileNotFoundError as e:
            print(f"❌ File missing: {e.filename}")
            exit(1)

    def clean_data(self, df):
        df = df.drop_duplicates()
        df = df.fillna(0)
        return df

    def generate_report(self):

        students, attendance = self.load_data()

        students = self.clean_data(students)
        attendance = self.clean_data(attendance)

        df = pd.merge(students, attendance, on="studentId", how="inner")

        df["status"] = df["marks"].apply(lambda x: "PASS" if x >= 50 else "FAIL")

        report_path = os.path.join(self.output_path, "report.csv")
        df.to_csv(report_path, index=False)

        summary = {
            "totalStudents": int(len(df)),
            "avgAttendance": float(df["attendancePercent"].mean()),
            "avgMarks": float(df["marks"].mean()),
            "passCount": int((df["status"] == "PASS").sum()),
            "failCount": int((df["status"] == "FAIL").sum()),
            "top3Students": df.sort_values(by="marks", ascending=False)
            .head(3)["name"]
            .tolist()
        }

        summary_path = os.path.join(self.output_path, "summary.json")

        with open(summary_path, "w") as f:
            json.dump(summary, f, indent=4)

        print("✅ Report Generated Successfully!")
        print(f"📄 {report_path}")
        print(f"📄 {summary_path}")