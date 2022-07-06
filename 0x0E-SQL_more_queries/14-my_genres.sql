-- Uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.

SELECT g.name FROM tv_shows AS s
	INNER JOIN tv_show_genres AS s_g
		ON s.id = s_g.show_id
	INNER JOIN tv_genres AS g
		ON s_g.genre_id = g.id
	WHERE s.title = "Dexter"
	ORDER BY g.name ASC;
