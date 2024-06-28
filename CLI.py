import subprocess as sp
import pymysql
import pymysql.cursors

def insertComment():
    try:
        row = {}
        print("Enter comment details: ")
        row["comment_id"] = input("Comment ID: ")
        row["viewer_email"] = input("Viewer's Email: ")
        row["date"] = input("Comment Date (YYYY-MM-DD): ")
        row["likes"] = int(input("Likes: "))
        row["content"] = input("Comment Content: ")
        row["video_id"] = input("Video ID: ")

        query = "INSERT INTO COMMENTS(comment_id, viewer_email, date, likes, content, video_id) VALUES ('%s', '%s', '%s', %d, '%s', '%s')" % (
            row["comment_id"], row["viewer_email"], row["date"], row["likes"], row["content"], row["video_id"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Comment Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert comment into the database")
        print(">>>>>>>>>>>>>", e)

def editComment():
    try:
        comment_id = input("Comment ID to edit: ")
        new_content = input("Enter new comment content: ")

        query = "UPDATE COMMENTS SET content='%s' WHERE comment_id='%s'" % (
            new_content, comment_id)

        print(query)
        cur.execute(query)
        con.commit()

        print("Comment Edited Successfully")

    except Exception as e:
        con.rollback()
        print("Failed to edit comment")
        print(">>>>>>>>>>>>>", e)

def changeVideoDescription():
    try:
        video_id = input("Video ID to edit: ")
        new_description = input("Enter new video description: ")

        query = "UPDATE VIDEOS SET description='%s' WHERE video_id='%s'" % (
            new_description, video_id)

        print(query)
        cur.execute(query)
        con.commit()

        print("Video Description Changed Successfully")

    except Exception as e:
        con.rollback()
        print("Failed to change video description")
        print(">>>>>>>>>>>>>", e)

def changeVideoTags():
    try:
        video_id = input("Video ID to edit: ")
        new_tags = input("Enter new tags (comma-separated): ")
        new_tags_list = [tag.strip() for tag in new_tags.split(',')]

        # Delete existing tags
        query_delete = "DELETE FROM VIDEO_TAGS WHERE video_id='%s'" % (video_id)
        cur.execute(query_delete)

        # Insert new tags
        for tag in new_tags_list:
            query_insert = "INSERT INTO VIDEO_TAGS(video_id, tag) VALUES ('%s', '%s')" % (
                video_id, tag)
            cur.execute(query_insert)

        con.commit()

        print("Video Tags Changed Successfully")

    except Exception as e:
        con.rollback()
        print("Failed to change video tags")
        print(">>>>>>>>>>>>>", e)

def deleteComment():
    try:
        comment_id = input("Comment ID to delete: ")

        query = "DELETE FROM COMMENTS WHERE comment_id='%s'" % (comment_id)

        print(query)
        cur.execute(query)
        con.commit()

        print("Comment Deleted Successfully")

    except Exception as e:
        con.rollback()
        print("Failed to delete comment")
        print(">>>>>>>>>>>>>", e)

def unlikeVideo():
    try:
        viewer_email = input("Viewer's Email: ")
        video_id = input("Video ID: ")

        query = "DELETE FROM VIEWER_LIKES_VIDEO_BY_CHANNEL_IN_PLAYLIST WHERE viewer_email_id='%s' AND video_id='%s'" % (
            viewer_email, video_id)

        print(query)
        cur.execute(query)
        con.commit()

        print("Video Unliked Successfully")

    except Exception as e:
        con.rollback()
        print("Failed to unlike the video")
        print(">>>>>>>>>>>>>", e)

def deletePlaylist():
    try:
        playlist_name = input("Playlist Name: ")
        
        query = "DELETE FROM PLAYLISTS WHERE name_of_playlist='%s'" % (
            playlist_name)

        print(query)
        cur.execute(query)
        con.commit()

        print("Playlist Deleted Successfully")

    except Exception as e:
        con.rollback()
        print("Failed to Delete Playlist")
        print(">>>>>>>>>>>>>", e)

def deleteVideo():
    try:
        video_id = input("Video ID to delete: ")

        query = "DELETE FROM VIDEOS WHERE video_id='%s'" % (video_id)

        print(query)
        cur.execute(query)
        con.commit()

        print("Video Deleted Successfully")

    except Exception as e:
        con.rollback()
        print("Failed to delete video")
        print(">>>>>>>>>>>>>", e)

def selectallchannelshavingmorethanxsubs():
    try:
        x = int(input("Enter x: "))

        query = "SELECT * FROM CHANNEL WHERE subscriber_count > %d" % (x)

        print(query)
        cur.execute(query)
        con.commit()

        print("Channels with more than %d subscribers:" % (x))
        for row in cur:
            print(row)

    except Exception as e:
        con.rollback()
        print("Failed to select channels")
        print(">>>>>>>>>>>>>", e)

def selectallchannelswhichproducextag():
    try:
        x = input("Enter x: ")

        query = "SELECT channel_name FROM (((CHANNEL NATURAL JOIN CHANNEL_VIDEOS) NATURAL JOIN VIDEOS) NATURAL JOIN VIDEO_TAGS) WHERE tag='%s'" % (x)

        print(query)
        cur.execute(query)
        con.commit()

        print("Channels which produce videos of the %s genre:" % (x))
        for row in cur:
            print(row)

    except Exception as e:
        con.rollback()
        print("Failed to select channels")
        print(">>>>>>>>>>>>>", e)

def selectallchannelsfromregionx():
    try:
        x = input("Enter x: ")

        query = "SELECT channel_name FROM CHANNEL WHERE region='%s'" % (x)

        print(query)
        cur.execute(query)
        con.commit()

        print("Channels from region %s:" % (x))
        for row in cur:
            print(row)

    except Exception as e:
        con.rollback()
        print("Failed to select channels")
        print(">>>>>>>>>>>>>", e)

def selectallchannelswhichuselanguagex():
    try:
        x = input("Enter x: ")

        query = "SELECT channel_name FROM CHANNEL WHERE language='%s'" % (x)

        print(query)
        cur.execute(query)
        con.commit()

        print("Channels which use %s language:" % (x))
        for row in cur:
            print(row)

    except Exception as e:
        con.rollback()
        print("Failed to select channels")
        print(">>>>>>>>>>>>>", e)

def usernamesofviewersofagex():
    try:
        x = int(input("Enter x: "))

        query = "SELECT email_id, age FROM (VIEWER NATURAL JOIN DOB_AGE) WHERE age='%s'" % (x)

        print(query)
        cur.execute(query)
        con.commit()

        print("Usernames of viewers who are of age %d:" % (x))
        for row in cur:
            print(row)

    except Exception as e:
        con.rollback()
        print("Failed to select viewers")
        print(">>>>>>>>>>>>>", e)

def emailidsofviewerssubbedtochannelx():
    try:
        x = input("Enter x: ")

        query = "SELECT viewer_email_id FROM VIEWER_SUBSCRIBES_TO_CHANNEL WHERE channel_name='%s'" % (x)

        print(query)
        cur.execute(query)
        con.commit()

        print("Email IDs of viewers who have subscribed to channel %s:" % (x))
        for row in cur:
            print(row)

    except Exception as e:
        con.rollback()
        print("Failed to select viewers")
        print(">>>>>>>>>>>>>", e)

def avgsharesreceivedbyvideosfromchannelx():
    try:
        x = input("Enter x: ")

        query = "SELECT AVG(shares) FROM ((CHANNEL NATURAL JOIN CHANNEL_VIDEOS) NATURAL JOIN VIDEOS) GROUP BY(channel_name) HAVING channel_name='%s'" % (x)

        print(query)
        cur.execute(query)
        con.commit()

        print("Average number of views received by videos from channel %s:" % (x))
        for row in cur:
            print(row)

    except Exception as e:
        con.rollback()
        print("Failed to select videos")
        print(">>>>>>>>>>>>>", e)

def medianvideodurationforchannelx(channel_name):
    try:
        # Calculate the rowindex
        query_rowindex = "SET @rowindex := -1;"
        cur.execute(query_rowindex)

        # Select the rowindex and video duration for the specified channel
        query_select = f"""
            SELECT
                AVG(d.duration) as Median
            FROM
                (SELECT @rowindex:=@rowindex + 1 AS rowindex,
                        VIDEOS.duration AS duration
                FROM VIDEOS
                JOIN CHANNEL_VIDEOS ON VIDEOS.video_id = CHANNEL_VIDEOS.video_id
                WHERE CHANNEL_VIDEOS.channel_name = '{channel_name}'
                ORDER BY VIDEOS.duration) AS d
            WHERE
            d.rowindex IN (FLOOR(@rowindex / 2), CEIL(@rowindex / 2));
        """

        cur.execute(query_select)
        result = cur.fetchone()

        if result:
            median_duration = result["Median"]
            print(f"Median Video Duration for Channel {channel_name}: {median_duration}")
        else:
            print(f"No videos found for Channel {channel_name}")

    except Exception as e:
        print("Error calculating median video duration")
        print(">>>>>>>>>>>>>", e)

def videoWithMostSharesByChannelX(channel_name):
    try:
        query = f"""
            SELECT
                VIDEOS.video_id,
                VIDEOS.title,
                VIDEOS.shares
            FROM
                VIDEOS
            JOIN CHANNEL_VIDEOS ON VIDEOS.video_id = CHANNEL_VIDEOS.video_id
            WHERE
                CHANNEL_VIDEOS.channel_name = '{channel_name}'
            ORDER BY
                VIDEOS.shares DESC
            LIMIT 1;
        """

        cur.execute(query)
        result = cur.fetchone()

        if result:
            video_id = result["video_id"]
            title = result["title"]
            shares = result["shares"]
            print(f"Video with Most Shares for Channel {channel_name}:")
            print(f"Video ID: {video_id}, Title: {title}, Shares: {shares}")
        else:
            print(f"No videos found for Channel {channel_name}")

    except Exception as e:
        print("Error retrieving video with most shares")
        print(">>>>>>>>>>>>>", e)

def searchForVideosByTitle():
    try:
        title_query = input("Enter part of the title to search for: ")
        query = f"""
            SELECT
                video_id,
                title,
                shares
            FROM
                VIDEOS
            WHERE
                title LIKE '%{title_query}%'
            ORDER BY
                shares DESC;
        """

        cur.execute(query)
        results = cur.fetchall()

        if results:
            print(f"Videos with Title containing '{title_query}':")
            for result in results:
                video_id = result["video_id"]
                title = result["title"]
                shares = result["shares"]
                print(f"Video ID: {video_id}, Title: {title}, Shares: {shares}")
        else:
            print(f"No videos found with Title containing '{title_query}'")

    except Exception as e:
        print("Error searching for videos by title")
        print(">>>>>>>>>>>>>", e)

def searchForVideosByMatchingTags():
    try:
        tag_query = input("Enter a tag to search for: ")
        query = f"""
            SELECT
                VIDEOS.video_id,
                VIDEOS.title,
                VIDEOS.shares
            FROM
                VIDEOS
            JOIN VIDEO_TAGS ON VIDEOS.video_id = VIDEO_TAGS.video_id
            WHERE
                VIDEO_TAGS.tag = '{tag_query}'
            ORDER BY
                VIDEOS.shares DESC;
        """

        cur.execute(query)
        results = cur.fetchall()

        if results:
            print(f"Videos with Tag '{tag_query}':")
            for result in results:
                video_id = result["video_id"]
                title = result["title"]
                shares = result["shares"]
                print(f"Video ID: {video_id}, Title: {title}, Shares: {shares}")
        else:
            print(f"No videos found with Tag '{tag_query}'")

    except Exception as e:
        print("Error searching for videos by matching tags")
        print(">>>>>>>>>>>>>", e)

def searchForVideosOfChannelXOfGenreYCreatedInLanguageZ():
    try:
        channel_name = input("Enter Channel Name: ")
        genre_query = input("Enter Genre (Tag): ")
        language_query = input("Enter Language: ")

        query = f"""
            SELECT
                VIDEOS.video_id,
                VIDEOS.title,
                VIDEOS.shares
            FROM
                (VIDEOS NATURAL JOIN CHANNEL_VIDEOS) NATURAL JOIN CHANNEL
            WHERE
                CHANNEL_VIDEOS.channel_name = '{channel_name}'
                AND CHANNEL.language = '{language_query}'
            ORDER BY
                VIDEOS.shares DESC;
        """

        cur.execute(query)
        results = cur.fetchall()

        if results:
            print(f"Videos for Channel {channel_name}, Genre '{genre_query}', Language '{language_query}':")
            for result in results:
                video_id = result["video_id"]
                title = result["title"]
                shares = result["shares"]
                print(f"Video ID: {video_id}, Title: {title}, Shares: {shares}")
        else:
            print(f"No videos found for Channel {channel_name}, Genre '{genre_query}', Language '{language_query}'")

    except Exception as e:
        print("Error searching for videos by channel, genre, and language")
        print(">>>>>>>>>>>>>", e)

def dispatch(ch):
    if(ch == 1):
        insertComment() # done
    elif(ch == 2):
        editComment() # done
    elif(ch == 3):
        changeVideoDescription() # done
    elif(ch == 4):
        changeVideoTags() # done
    elif(ch == 5):
        deleteComment() # done
    elif(ch == 6):
        unlikeVideo() # done
    elif(ch == 7):
        deletePlaylist()  # done
    elif(ch == 8):
        deleteVideo() # done
    elif(ch == 9):
        selectallchannelshavingmorethanxsubs() # done
    elif(ch == 10):
        selectallchannelswhichproducextag() # done
    elif(ch == 11):
        selectallchannelsfromregionx() # done
    elif(ch == 12):
        selectallchannelswhichuselanguagex() # done
    elif(ch == 13):
        usernamesofviewersofagex() # done
    elif(ch == 14):
        emailidsofviewerssubbedtochannelx() # done
    elif(ch == 19):
        avgsharesreceivedbyvideosfromchannelx() # done
    elif(ch == 20):
        channel_name = input("Enter Channel Name: ")
        medianvideodurationforchannelx(channel_name) # done
    elif(ch == 15):
        channel_name = input("Enter Channel Name: ")
        videoWithMostSharesByChannelX(channel_name) # done
    elif(ch == 16):
        searchForVideosByTitle() # done
    elif(ch == 17):
        searchForVideosByMatchingTags() #done
    elif(ch == 18):
        searchForVideosOfChannelXOfGenreYCreatedInLanguageZ() # done
    else:
        print("Error: Invalid Option")


# Global
while(1):
    tmp = sp.call('clear', shell=True)
    
    # Can be skipped if you want to hardcode username and password
    # username = input("Username: ")
    # password = input("Password: ")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server 
        con = pymysql.connect(host='localhost',
                              port=3306,
                              user="root",
                              #password="new_password",
                              db='YouTube_DB',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear', shell=True)
                print("<-- Modifications -->")
                print("1. Insert a Comment") # TAYA
                print("2. Edit a Comment") # TAYA
                print("3. Change Video Description") # TAYA
                print("4. Change Video Tags") # TAYA
                print("5. Delete a Comment") # ARUSH
                print("6. Unlike a Video") # ARUSH
                print("7. Delete a Playlist") # ARUSH
                print("8. Make a Video Private") # ARUSH
                print("")
                print("<-- Retrievals -->")
                print("9. Select all channels having more than ”x” subscribers.") # ARUSH
                print("10. Select all channels which produce videos of the ”x” genre (tag).") # ARUSH
                print("11. Select all channels from region ”x”.") # ARUSH
                print("12. Select all channels which produce videos in ”x” language.") # ARUSH
                print("13. Usernames of viewers who are of age ”x”.") # ARUSH
                print("14. Email ids of viewers who have subscribed to channel ”x”.") # ARUSH
                print("15. Video with most shares by channel ”x”.") #TAYA
                print("16. Search for videos by title (auto-complete).") #TAYA
                print("17. Search for videos by matching tags.") #TAYA
                print("18. Search for videos of channel ”x” of genre (tag) ”y” created in language ”z”") #TAYA
                print("")
                print("<-- Analysis -->")
                print("19. Average number of shares received by videos from channel ”x.”") # ARUSH
                print("20. Median video duration for channel ”x.”") #TAYA
                print("")
                print("21. Logout")
                print("")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 21:
                    exit()
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
