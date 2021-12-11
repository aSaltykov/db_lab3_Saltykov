DO $$
DECLARE
    artist_id   	  artist.artist_id%TYPE;
    artist_name 	  artist.artist_name%TYPE;

BEGIN
    artist_id := 20;
    artist_name := 'CertainArtist';
    FOR counter IN 1..10
        LOOP
            INSERT INTO artist(artist_id, artist_name)
            VALUES (counter + artist_id, artist_name || counter);
        END LOOP;
END;
$$