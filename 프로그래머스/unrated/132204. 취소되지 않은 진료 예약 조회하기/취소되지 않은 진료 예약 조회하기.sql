-- 코드를 입력하세요
SELECT B.APNT_NO, A.PT_NAME, A.PT_NO, B.MCDP_CD, C.DR_NAME , B.APNT_YMD
FROM PATIENT A, APPOINTMENT B, DOCTOR C
WHERE 1=1
AND A.PT_NO = B.PT_NO
AND C.DR_ID = B.MDDR_ID
AND C.MCDP_CD = 'CS'
AND TO_CHAR(B.APNT_YMD,'YYYYMMDD')='20220413'
AND B.APNT_CNCL_YN = 'N'
ORDER BY APNT_YMD