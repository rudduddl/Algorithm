-- 코드를 입력하세요
SELECT
    b.TITLE,
    b.BOARD_ID,
    r.REPLY_ID,
    r.WRITER_ID,
    r.CONTENTS,
    DATE_FORMAT(r.CREATED_DATE, '%Y-%m-%d') AS CREATED_DATE
FROM
    USED_GOODS_REPLY AS r
LEFT JOIN 
    USED_GOODS_BOARD AS b ON b.BOARD_ID = r.BOARD_ID
WHERE
    DATE(b.CREATED_DATE) BETWEEN '2022-10-01' AND '2022-10-31'
ORDER BY
    r.CREATED_DATE, b.TITLE;