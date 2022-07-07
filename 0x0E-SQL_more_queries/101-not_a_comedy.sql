-- Lists all shows without the genre Comedy in the database hbtn_0d_tvshows.

SELECT DISTINCT s.title FROM tv_shows AS s
	LEFT JOIN tv_show_genres AS s_g
		ON s.id = s_g.show_id
	WHERE s.title NOT IN (
		SELECT s.title FROM tv_genres AS g
		INNER JOIN tv_show_genres AS s_g
			ON g.id = s_g.genre_id
		INNER JOIN tv_shows AS s
			ON s_g.show_id = s.id
		WHERE g.name = "Comedy"
	)
	ORDER BY s.title ASC;
