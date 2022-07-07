-- Uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter

SELECT DISTINCT g.name FROM tv_genres AS g
	INNER JOIN tv_show_genres AS s_g
		ON g.id = s_g.genre_id
	WHERE g.name NOT IN (
		SELECT g.name FROM tv_shows AS s
		INNER JOIN tv_show_genres AS s_g
			ON s.id = s_g.show_id
		INNER JOIN tv_genres AS g
			ON s_g.genre_id = g.id
		WHERE s.title = "Dexter"
	)
	ORDER BY g.name ASC;
