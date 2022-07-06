-- Lists all Comedy shows in the database hbtn_0d_tvshows.

SELECT s.title FROM tv_genres AS g
	INNER JOIN tv_show_genres AS s_g
		ON g.id = s_g.genre_id
	INNER JOIN tv_shows AS s
		ON s_g.show_id = s.id
	WHERE g.name = "Comedy"
	ORDER BY s.title ASC;
