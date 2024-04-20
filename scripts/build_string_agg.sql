DROP TABLE IF EXISTS #StringTable
CREATE TABLE #StringTable
(
    BusinessEntityIDs VARCHAR(MAX)
    ,FirstName NVARCHAR(50)
)

INSERT INTO #StringTable
SELECT STRING_AGG(BusinessEntityID, ', ') As IDs
		,p.FirstName
FROM [AdventureWorks2022].[Person].[Person] p
GROUP BY p.FirstName
ORDER BY p.FirstName ASC;


SELECT string_split( BusinessEntityIDs, ',') AS BusinessEntityID
        ,FirstName
FROM #StringTable;

SELECT BusinessEntityID, FirstName
FROM #StringTable
CROSS APPLY (SELECT value FROM BusinessEntityIDs) AS BusinessEntityID;