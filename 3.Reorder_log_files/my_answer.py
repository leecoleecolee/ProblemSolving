from typing import List


class Solution:
    def reorder_log_files(self, logs: List[str]) -> List[str]:
        digit_log = []
        for idx, log in enumerate(logs):
            if log[:3] == "dig":
                digit_log.append(log)
                del logs[idx]
        logs.sort()
        logs += digit_log
        return logs


if __name__ == "__main__":
    s = Solution()
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
            "let2 own kit dig", "let3 art zero"]
    ret_logs = s.reorder_log_files(logs)
    print(ret_logs)
