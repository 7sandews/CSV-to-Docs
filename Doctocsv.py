import re
import pandas as pd

# Reusing the complete MCQ string from the user's message instead of reading from a file

full_text = """
1. What is 92% of 73?
A. 62.16
B. 75.16
C. 80.16
D. 67.16
Answer: 67.16

2. What is 49% of 92?
A. 36.08
B. 45.08
C. 56.08
D. 49.08
Answer: 45.08

3. What is 77% of 33?
A. 25.41
B. 17.41
C. 36.41
D. 30.41
Answer: 25.41

4. What is 29% of 49?
A. 12.21
B. 31.21
C. 24.21
D. 14.21
Answer: 14.21

5. What is 88% of 60?
A. 52.8
B. 43.8
C. 56.8
D. 71.8
Answer: 52.8

6. What is 98% of 64?
A. 66.72
B. 62.72
C. 59.72
D. 74.72
Answer: 62.72

7. What is 59% of 71?
A. 45.89
B. 41.89
C. 40.89
D. 61.89
Answer: 41.89

8. What is 38% of 40?
A. 17.2
B. 8.2
C. 15.2
D. 28.2
Answer: 15.2

9. What is 79% of 78?
A. 61.62
B. 53.62
C. 75.62
D. 67.62
Answer: 61.62

10. What is 54% of 17?
A. 9.18
B. -0.8200000000000003
C. 19.18
D. 22.18
Answer: 9.18

11. What is 72% of 78?
A. 66.16
B. 56.16
C. 46.16
D. 76.16
Answer: 56.16

12. What is 74% of 12?
A. 8.88
B. 2.880000000000001
C. 26.880000000000003
D. 9.88
Answer: 8.88

13. What is 65% of 18?
A. 9.7
B. 11.7
C. 14.7
D. 22.7
Answer: 11.7

14. What is 23% of 25?
A. 20.75
B. 13.75
C. 1.75
D. 5.75
Answer: 5.75

15. What is 41% of 99?
A. 30.590000000000003
B. 40.59
C. 47.59
D. 60.59
Answer: 40.59

16. What is 24% of 76?
A. 18.24
B. 17.24
C. 38.239999999999995
D. 28.24
Answer: 18.24

17. What is 31% of 63?
A. 17.53
B. 24.53
C. 19.53
D. 37.53
Answer: 19.53

18. What is 13% of 23?
A. 2.99
B. 16.990000000000002
C. 0.9900000000000002
D. 7.99
Answer: 2.99

19. What is 20% of 27?
A. 6.4
B. 16.4
C. 4.4
D. 5.4
Answer: 5.4

20. What is 89% of 25?
A. 19.25
B. 24.25
C. 22.25
D. 37.25
Answer: 22.25

21. What is 94% of 24?
A. 42.56
B. 16.56
C. 22.56
D. 23.56
Answer: 22.56

22. What is 53% of 19?
A. 2.0700000000000003
B. 10.07
C. 19.07
D. 23.07
Answer: 10.07

23. What is 1% of 89?
A. 0.89
B. 7.89
C. 13.89
D. -0.10999999999999999
Answer: 0.89

24. What is 82% of 66?
A. 66.12
B. 55.12
C. 54.12
D. 53.12
Answer: 54.12

25. What is 4% of 40?
A. -6.4
B. 9.6
C. 18.6
D. 1.6
Answer: 1.6

26. What is 89% of 58?
A. 44.62
B. 51.62
C. 70.62
D. 55.62
Answer: 51.62

27. What is 31% of 89?
A. 31.59
B. 45.59
C. 27.59
D. 17.59
Answer: 27.59

28. What is 46% of 16?
A. 0.3600000000000003
B. 17.36
C. 21.36
D. 7.36
Answer: 7.36

29. What is 60% of 15?
A. 9.0
B. 15.0
C. -1.0
D. 23.0
Answer: 9.0

30. What is 17% of 42?
A. 20.14
B. 15.14
C. -2.8600000000000003
D. 7.14
Answer: 7.14

31. What is 75% of 38?
A. 46.5
B. 28.5
C. 21.5
D. 29.5
Answer: 28.5

32. What is 17% of 10?
A. -1.3
B. 9.7
C. 12.7
D. 1.7
Answer: 1.7

33. What is 36% of 85?
A. 30.6
B. 41.6
C. 27.6
D. 39.6
Answer: 30.6

34. What is 82% of 34?
A. 29.88
B. 27.88
C. 18.88
D. 40.879999999999995
Answer: 27.88

35. What is 90% of 11?
A. 6.9
B. 21.9
C. 15.9
D. 9.9
Answer: 9.9

36. What is 63% of 52?
A. 32.76
B. 39.76
C. 51.76
D. 27.759999999999998
Answer: 32.76

37. What is 91% of 69?
A. 80.78999999999999
B. 52.79
C. 66.78999999999999
D. 62.79
Answer: 62.79

38. What is 58% of 51?
A. 29.58
B. 42.58
C. 28.58
D. 39.58
Answer: 29.58

39. What is 81% of 58?
A. 55.98
B. 39.98
C. 46.98
D. 59.98
Answer: 46.98

40. What is 65% of 31?
A. 15.149999999999999
B. 22.15
C. 20.15
D. 38.15
Answer: 20.15

41. What is 47% of 41?
A. 36.269999999999996
B. 19.27
C. 11.27
D. 29.27
Answer: 19.27

42. What is 61% of 31?
A. 15.91
B. 31.91
C. 26.91
D. 18.91
Answer: 18.91

43. What is 17% of 36?
A. -2.88
B. 6.12
C. 12.120000000000001
D. 18.12
Answer: 6.12

44. What is 2% of 62?
A. 15.24
B. 1.24
C. 9.24
D. -3.76
Answer: 1.24

45. What is 39% of 82?
A. 41.980000000000004
B. 50.980000000000004
C. 30.98
D. 31.98
Answer: 31.98

46. What is 63% of 44?
A. 32.72
B. 27.72
C. 18.72
D. 46.72
Answer: 27.72

47. What is 19% of 50?
A. 20.5
B. 7.5
C. 13.5
D. 9.5
Answer: 9.5

48. What is 31% of 99?
A. 33.69
B. 29.69
C. 47.69
D. 30.69
Answer: 30.69

49. What is 75% of 64?
A. 48.0
B. 63.0
C. 45.0
D. 58.0
Answer: 48.0

50. What is 9% of 52?
A. 24.68
B. 14.68
C. 3.6799999999999997
D. 4.68
Answer: 4.68

51. What is 99% of 89?
A. 95.11
B. 88.11
C. 80.11
D. 105.11
Answer: 88.11

52. What is 94% of 64?
A. 71.16
B. 67.16
C. 60.16
D. 50.16
Answer: 60.16

53. What is 76% of 15?
A. 23.4
B. 13.4
C. 11.4
D. 7.4
Answer: 11.4

54. What is 57% of 87?
A. 43.59
B. 51.59
C. 49.59
D. 65.59
Answer: 49.59

55. What is 20% of 14?
A. 7.8
B. 0.7999999999999998
C. 2.8
D. 21.8
Answer: 2.8

56. What is 9% of 50?
A. 4.5
B. 7.5
C. 16.5
D. 3.5
Answer: 4.5

57. What is 12% of 81?
A. 9.72
B. 27.72
C. 6.720000000000001
D. 14.72
Answer: 9.72

58. What is 33% of 56?
A. 23.48
B. 16.48
C. 18.48
D. 37.480000000000004
Answer: 18.48

59. What is 86% of 72?
A. 78.92
B. 61.92
C. 69.92
D. 58.92
Answer: 61.92

60. What is 93% of 38?
A. 40.34
B. 52.34
C. 35.34
D. 34.34
Answer: 35.34

61. What is 27% of 92?
A. 32.84
B. 24.84
C. 19.84
D. 35.84
Answer: 24.84

62. What is 97% of 18?
A. 9.46
B. 17.46
C. 37.46
D. 20.46
Answer: 17.46

63. What is 55% of 62?
A. 26.1
B. 34.1
C. 43.1
D. 50.1
Answer: 34.1

64. What is 19% of 30?
A. 10.7
B. 0.7000000000000002
C. 5.7
D. 21.7
Answer: 5.7

65. What is 10% of 90?
A. 2.0
B. 9.0
C. 28.0
D. 12.0
Answer: 9.0

66. What is 68% of 42?
A. 35.56
B. 40.56
C. 26.56
D. 28.56
Answer: 28.56

67. What is 77% of 41?
A. 43.57
B. 31.57
C. 38.57
D. 30.57
Answer: 31.57

68. What is 73% of 96?
A. 70.08
B. 71.08
C. 89.08
D. 63.08
Answer: 70.08

69. What is 8% of 94?
A. 7.52
B. -0.4800000000000004
C. 10.52
D. 20.52
Answer: 7.52

70. What is 21% of 36?
A. 1.5599999999999996
B. 12.559999999999999
C. 25.56
D. 7.56
Answer: 7.56

71. What is 96% of 10?
A. 14.6
B. 8.6
C. 9.6
D. 29.6
Answer: 9.6

72. What is 3% of 84?
A. -0.48
B. 2.52
C. 11.52
D. 14.52
Answer: 2.52

73. What is 5% of 84?
A. 20.2
B. -1.7999999999999998
C. 10.2
D. 4.2
Answer: 4.2

74. What is 33% of 38?
A. 19.54
B. 12.54
C. 32.54
D. 4.539999999999999
Answer: 12.54

75. What is 57% of 65?
A. 43.05
B. 27.049999999999997
C. 37.05
D. 51.05
Answer: 37.05

76. What is 72% of 52?
A. 37.44
B. 48.44
C. 28.439999999999998
D. 38.44
Answer: 37.44

77. What is 20% of 78?
A. 17.6
B. 15.6
C. 14.6
D. 26.6
Answer: 15.6

78. What is 42% of 74?
A. 33.08
B. 46.08
C. 30.08
D. 31.08
Answer: 31.08

79. What is 95% of 42?
A. 39.9
B. 38.9
C. 54.9
D. 41.9
Answer: 39.9

80. What is 87% of 46?
A. 40.02
B. 42.02
C. 53.02
D. 35.02
Answer: 40.02

81. What is 53% of 65?
A. 32.45
B. 49.45
C. 34.45
D. 37.45
Answer: 34.45

82. What is 38% of 97?
A. 36.86
B. 48.86
C. 35.86
D. 44.86
Answer: 36.86

83. What is 5% of 89?
A. 24.45
B. 4.45
C. 14.45
D. -3.55
Answer: 4.45

84. What is 47% of 50?
A. 23.5
B. 28.5
C. 14.5
D. 37.5
Answer: 23.5

85. What is 81% of 82?
A. 66.42
B. 70.42
C. 63.42
D. 84.42
Answer: 66.42

86. What is 43% of 96?
A. 57.28
B. 41.28
C. 51.28
D. 37.28
Answer: 41.28

87. What is 53% of 11?
A. 3.83
B. 21.83
C. 5.83
D. 9.83
Answer: 5.83

88. What is 1% of 83?
A. 5.83
B. 0.83
C. 15.83
D. -0.17000000000000004
Answer: 0.83

89. What is 17% of 41?
A. 12.969999999999999
B. 6.97
C. 17.97
D. 0.9699999999999998
Answer: 6.97

90. What is 45% of 32?
A. 30.4
B. 14.4
C. 13.4
D. 21.4
Answer: 14.4

91. What is 22% of 63?
A. 13.86
B. 3.8599999999999994
C. 21.86
D. 24.86
Answer: 13.86

92. What is 95% of 22?
A. 38.9
B. 11.899999999999999
C. 30.9
D. 20.9
Answer: 20.9

93. What is 43% of 85?
A. 54.55
B. 36.55
C. 35.55
D. 46.55
Answer: 36.55

94. What is 29% of 96?
A. 27.84
B. 41.84
C. 18.84
D. 30.84
Answer: 27.84

95. What is 35% of 62?
A. 34.7
B. 24.7
C. 20.7
D. 21.7
Answer: 21.7

96. What is 51% of 56?
A. 44.56
B. 28.56
C. 30.56
D. 27.56
Answer: 28.56

97. What is 39% of 42?
A. 32.379999999999995
B. 17.38
C. 12.379999999999999
D. 16.38
Answer: 16.38

98. What is 79% of 44?
A. 30.759999999999998
B. 35.76
C. 48.76
D. 34.76
Answer: 34.76

99. What is 95% of 84?
A. 70.8
B. 92.8
C. 87.8
D. 79.8
Answer: 79.8

100. What is 69% of 47?
A. 23.43
B. 32.43
C. 37.43
D. 47.43
Answer: 32.43
"""

# Extracting 100 MCQs from the raw text
pattern = r"\d+\.\s(.*?)\nA\.\s(.*?)\nB\.\s(.*?)\nC\.\s(.*?)\nD\.\s(.*?)\nAnswer:\s(.*?)\n"
matches = re.findall(pattern, full_text, re.DOTALL)

# Create structured data
data_full = []
for match in matches:
    question, c1, c2, c3, c4, answer = match
    data_full.append({
        "Question": question.strip(),
        "Answer": answer.strip(),
        "Choice1": c1.strip(),
        "Choice2": c2.strip(),
        "Choice3": c3.strip(),
        "Choice4": c4.strip()
    })

df_full = pd.DataFrame(data_full)

# Save to CSV
full_file_path = "/Users/soumya/Downloads/finalpercentage_mcqs_100.csv"
df_full.to_csv(full_file_path, index=False)

# Display for user
# tools.display_dataframe_to_user(name="Percentage MCQs (100)", dataframe=df_full)

full_file_path