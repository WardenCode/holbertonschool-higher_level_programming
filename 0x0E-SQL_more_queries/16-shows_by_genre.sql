-- Lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.

SELECT s.title, g.name FROM tv_genres AS g
	INNER JOIN tv_show_genres AS s_g
		ON g.id = s_g.genre_id
	RIGHT JOIN tv_shows AS s
		ON s_g.show_id = s.id
	ORDER BY s.title ASC, g.name ASC;
