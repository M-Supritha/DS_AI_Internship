raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]
unique_users = set(raw_logs)
is_id05_present = "ID05" in unique_users
print("Is ID05 present in unique users?", is_id05_present)
print("Total log entries:", len(raw_logs))
print("Unique users:", len(unique_users))
print("Unique User IDs:", unique_users)