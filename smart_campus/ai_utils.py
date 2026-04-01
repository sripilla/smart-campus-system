def predict_performance(attendance, marks):
    if attendance >= 75 and marks >= 70:
        return "Excellent ✅"
    elif attendance >= 60 and marks >= 50:
        return "Average ⚖️"
    else:
        return "At Risk ⚠️"