USE db_puscgce;
INSERT INTO texts (title, author, language, created_at, body, word_count, status)
VALUES ('Demo', 'Angel', 'es', NOW(), 'Hola mundo desde MySQL en Cloud SQL', 7, 'NEW');

SELECT id, title, language, word_count, status
FROM texts ORDER BY id DESC LIMIT 5;

UPDATE texts
SET status='READY', updated_at=NOW()
WHERE status='NEW'
ORDER BY id DESC
LIMIT 1;

SELECT id, title, status, updated_at
FROM texts ORDER BY id DESC LIMIT 5;

DELETE FROM texts
WHERE status='READY'
ORDER BY id DESC
LIMIT 1;
