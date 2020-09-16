# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    739.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sanam <marvin@42.fr>                       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/09/11 00:37:07 by sanam             #+#    #+#              #
#    Updated: 2020/09/11 01:48:48 by sanam            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from typing import *

class Solution:
        def dailyTemperatures(self, T: List[int]) -> List[int]:
            answer = [0] * len(T)
            stack = []
            for i, cur in enumerate(T):
                while stack and cur > T[stack[-1]]:
                    last = stack.pop()
                    answer[last] = i - last
                stack.append(i)
            return answer


if __name__ == "__main__":
    sol = Solution()
    print(sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    
