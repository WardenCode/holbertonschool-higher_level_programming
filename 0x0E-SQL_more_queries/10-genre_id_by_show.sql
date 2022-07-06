-- Lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.

SELECT s.title, s_g.genre_id FROM tv_shows AS s
	INNER JOIN tv_show_genres AS s_g
	ON s.id = s_g.show_id
	ORDER BY s.title ASC, s_g.genre_id ASC;
