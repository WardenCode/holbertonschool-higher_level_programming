-- Lists all genres in the database hbtn_0d_tvshows_rate by their rating.

SELECT g.name, SUM(s_r.rate) AS rating FROM tv_shows AS s
	INNER JOIN tv_show_ratings AS s_r
		ON s.id = s_r.show_id
	INNER JOIN tv_show_genres AS s_g
		ON s.id = s_g.show_id
	INNER JOIN tv_genres AS g
		ON g.id = s_g.genre_id
	GROUP BY g.name
	ORDER BY rating DESC;
