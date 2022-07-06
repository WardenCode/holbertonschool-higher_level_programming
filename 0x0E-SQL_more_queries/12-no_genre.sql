-- Lists all shows contained in hbtn_0d_tvshows without a genre linked.

SELECT s.title, s_g.genre_id FROM tv_shows AS s
	LEFT JOIN tv_show_genres AS s_g
	ON s.id = s_g.show_id
	WHERE s_g.show_id IS NULL
	ORDER BY s.title ASC, s_g.genre_id ASC;

