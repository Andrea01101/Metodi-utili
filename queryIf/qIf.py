
Query con if:
select s.id as s1id, s2.id as s2id, case
	when s2.longitude > s.longitude then s2.longitude - s.longitude
	else s.longitude - s2.longitude
end
as peso
from sighting s, sighting s2
where year(s2.`datetime`) = year(s.`datetime`) and year(s.`datetime`) = 2004
and s.state = s2.state and s.shape = s2.shape and s.shape = 'disk'
and s.longitude<s2.longitude
order by s1id, s2id