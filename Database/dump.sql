DROP DATABASE IF EXISTS `YouTube_DB`;
CREATE SCHEMA `YouTube_DB`;
USE `YouTube_DB`;

-- Creating VIEWER table
CREATE TABLE VIEWER (
  email_id VARCHAR(255) PRIMARY KEY,
  date_of_birth DATE,
  region INT
);

-- Inserting data into VIEWER table
INSERT INTO VIEWER VALUES
  ('viewer1@example.com', '1990-01-15',  1),
  ('viewer2@example.com', '1985-05-22',  2),
  ('viewer3@example.com', '2000-09-10',  3),
  ('viewer4@example.com', '1995-03-03',  1),
  ('viewer5@example.com', '1988-11-28',  2);

-- Creating CHANNEL table
CREATE TABLE CHANNEL (
  channel_name VARCHAR(255) PRIMARY KEY,
  subscriber_count INT,
  region INT,
  language VARCHAR(50),
  average_income decimal(10,2)
);

-- Inserting data into CHANNEL table
INSERT INTO CHANNEL VALUES
  ('Channel1', 500000, 1, 'English', 10000.00),
  ('Channel2', 800000, 2, 'Spanish', 12000.50),
  ('Channel3', 300000, 3, 'French', 8000.75),
  ('Channel4', 700000, 1, 'English', 11000.25),
  ('Channel5', 600000, 2, 'German', 9500.50);

-- Creating VIDEOS table
CREATE TABLE VIDEOS (
  video_id VARCHAR(255) PRIMARY KEY,
  title VARCHAR(255),
  duration VARCHAR(20),
  shares INT,
  description TEXT,
  revenue_generated decimal(10, 2),
  monetary_status TINYINT(1)
);

-- Inserting data into VIDEOS table
INSERT INTO VIDEOS VALUES
  ('video1', 'Introduction to AI', '10:30', 5000, 'An overview of AI concepts', 2000.50, 1),
  ('video2', 'Web Development Basics', '15:45', 8000, 'Fundamental concepts of web development', 3000.75, 1),
  ('video3', 'French Cuisine Tutorial', '12:20', 3000, 'Cooking classic French dishes', 1500.25, 1),
  ('video4', 'Travel Vlog: New York City', '20:15', 7000, 'Exploring the Big Apple', 2500.00, 1),
  ('video5', 'Learning German: Lesson 1', '8:55', 4000, 'Basic German language lesson', 1800.50, 1);

-- Creating VIDEO_TAGS table
CREATE TABLE VIDEO_TAGS (
  video_id VARCHAR(255) REFERENCES VIDEOS(video_id) ON DELETE CASCADE,
  tag VARCHAR(255),
  PRIMARY KEY (video_id, tag)
);

-- Inserting data into VIDEO_TAGS table
INSERT INTO VIDEO_TAGS VALUES
  ('video1', 'AI'),
  ('video1', 'Technology'),
  ('video2', 'Web Development'),
  ('video3', 'Cooking'),
  ('video4', 'Travel');

-- Creating SHORTS table

CREATE TABLE SHORTS (
  short_id VARCHAR(255) PRIMARY KEY,
  title VARCHAR(255),
  duration VARCHAR(20),
  shares INT,
  revenue_generated decimal(10,2),
  monetary_status TINYINT(1)
);

-- Inserting data into SHORTS table
INSERT INTO SHORTS VALUES
  ('short1', 'Quick Coding Tips', '2:45', 2000, 500.25, 1),
  ('short2', 'Beautiful Sunset', '1:30', 1500, 300.50, 1),
  ('short3', 'French Dessert Recipe', '3:10', 1000, 250.75, 1),
  ('short4', 'NYC Times Square', '1:15', 1800, 400.00, 1),
  ('short5', 'Common German Phrases', '2:00', 1200, 350.50, 1);

-- Creating SPONSORS table
CREATE TABLE SPONSORS (
  sponsor_name VARCHAR(255) PRIMARY KEY,
  contact_info_id INT REFERENCES contact_info(contact_info_id) ON DELETE CASCADE,
  category_or_niche VARCHAR(255)
);

-- Inserting data into SPONSORS table
INSERT INTO SPONSORS VALUES
  ('Sponsor1', 1, 'Technology'),
  ('Sponsor2', 2, 'Travel'),
  ('Sponsor3', 3, 'Cooking'),
  ('Sponsor4', 4, 'Education'),
  ('Sponsor5', 5, 'Language Learning');

-- Creating contact_info table
CREATE TABLE contact_info (
  contact_info_id INT PRIMARY KEY,
  email_id VARCHAR(255),
  address VARCHAR(255)
);

-- Inserting data into contact_info table
INSERT INTO contact_info VALUES
  (1, 'sponsor1@example.com', '123 Tech Street'),
  (2, 'sponsor2@example.com', '456 Travel Avenue'),
  (3, 'sponsor3@example.com', '789 Cooking Lane'),
  (4, 'sponsor4@example.com', '101 Education Road'),
  (5, 'sponsor5@example.com', '202 Language Boulevard');

-- Creating phone_number table with phone_number length constraint
CREATE TABLE phone_number (
  contact_info_id INT REFERENCES contact_info(contact_info_id) ON DELETE CASCADE,
  phone_number BIGINT,
  PRIMARY KEY (contact_info_id, phone_number),
  CONSTRAINT check_phone_length CHECK (LENGTH(phone_number) = 10)
);

-- Inserting data into phone_number table
INSERT INTO phone_number VALUES
  (1, 1234567890),
  (2, 9876543210),
  (3, 5555555555),
  (4, 1111222233),
  (5, 9999999999);

-- Creating COMMENTS table
CREATE TABLE COMMENTS (
  comment_id VARCHAR(255) PRIMARY KEY,
  viewer_email VARCHAR(255) REFERENCES VIEWER(email_id) ON DELETE CASCADE,
  date DATE,
  likes INT,
  content TEXT,
  video_id VARCHAR(255) REFERENCES VIDEOS(video_id) ON DELETE CASCADE
);

-- Inserting data into COMMENTS table
INSERT INTO COMMENTS VALUES
  ('comment1', 'viewer1@example.com', '2023-01-05', 20, 'Great video!', 'video1'),
  ('comment2', 'viewer2@example.com', '2023-02-10', 15, 'I learned a lot from this.', 'video2'),
  ('comment3', 'viewer3@example.com', '2023-03-15', 25, 'Amazing content!', 'video3'),
  ('comment4', 'viewer4@example.com', '2023-04-20', 18, 'Keep up the good work.', 'video2'),
  ('comment5', 'viewer5@example.com', '2023-05-25', 22, 'This is my favorite channel!', 'video1');

-- Creating PLAYLISTS table
CREATE TABLE PLAYLISTS (
  name_of_playlist VARCHAR(255) PRIMARY KEY,
  creator_email VARCHAR(255) REFERENCES VIEWER(email_id) ON DELETE CASCADE,
  number_of_likes INT
);

-- Inserting data into PLAYLISTS table
INSERT INTO PLAYLISTS VALUES
  ('Tech Favorites', 'viewer1@example.com', 50),
  ('Travel Adventures', 'viewer2@example.com', 40),
  ('Cooking Delights', 'viewer3@example.com', 35),
  ('Educational Insights', 'viewer4@example.com', 45),
  ('Language Learning Journey', 'viewer5@example.com', 55);

-- Creating VIEWER_COMMENTS_ON_SHORTS_BY_CHANNEL table
CREATE TABLE VIEWER_COMMENTS_ON_SHORTS_BY_CHANNEL (
  viewer_email_id VARCHAR(255),
  short_id VARCHAR(255),
  channel_name VARCHAR(255),
  PRIMARY KEY (viewer_email_id, short_id, channel_name),
  FOREIGN KEY (viewer_email_id) REFERENCES VIEWER(email_id) ON DELETE CASCADE,
  FOREIGN KEY (short_id) REFERENCES SHORTS(short_id) ON DELETE CASCADE,
  FOREIGN KEY (channel_name) REFERENCES CHANNEL(channel_name) ON DELETE CASCADE
);

-- Inserting data into VIEWER_COMMENTS_ON_SHORTS_BY_CHANNEL table
INSERT INTO VIEWER_COMMENTS_ON_SHORTS_BY_CHANNEL VALUES
  ('viewer1@example.com', 'short3', 'Channel2'),
  ('viewer2@example.com', 'short4', 'Channel4'),
  ('viewer3@example.com', 'short1', 'Channel3'),
  ('viewer4@example.com', 'short5', 'Channel1'),
  ('viewer5@example.com', 'short2', 'Channel5');

-- Creating SPONSOR_SPONSORS_VIDEO_BY_CHANNEL table
CREATE TABLE SPONSOR_SPONSORS_VIDEO_BY_CHANNEL (
  sponsor_name VARCHAR(255),
  video_id VARCHAR(255),
  channel_name VARCHAR(255),
  PRIMARY KEY (sponsor_name, video_id, channel_name),
  FOREIGN KEY (sponsor_name) REFERENCES SPONSORS(sponsor_name) ON DELETE CASCADE,
  FOREIGN KEY (video_id) REFERENCES VIDEOS(video_id) ON DELETE CASCADE,
  FOREIGN KEY (channel_name) REFERENCES CHANNEL(channel_name) ON DELETE CASCADE
);

-- Inserting data into SPONSOR_SPONSORS_VIDEO_BY_CHANNEL table
INSERT INTO SPONSOR_SPONSORS_VIDEO_BY_CHANNEL VALUES
  ('Sponsor1', 'video2', 'Channel3'),
  ('Sponsor2', 'video4', 'Channel1'),
  ('Sponsor3', 'video1', 'Channel4'),
  ('Sponsor4', 'video5', 'Channel2'),
  ('Sponsor5', 'video3', 'Channel5');

-- Creating VIEWER_CHANNEL_SUBSCRIPTION table
CREATE TABLE VIEWER_CHANNEL_SUBSCRIPTION (
  subscription_id INT PRIMARY KEY,
  viewer_email_id VARCHAR(255),
  channel_name VARCHAR(255),
  subscription_date DATE,
  FOREIGN KEY (viewer_email_id) REFERENCES VIEWER(email_id) ON DELETE CASCADE,
  FOREIGN KEY (channel_name) REFERENCES CHANNEL(channel_name) ON DELETE CASCADE
);

-- Inserting data into VIEWER_CHANNEL_SUBSCRIPTION table
INSERT INTO VIEWER_CHANNEL_SUBSCRIPTION VALUES
  (1, 'viewer1@example.com', 'Channel1', '2023-01-01'),
  (2, 'viewer2@example.com', 'Channel2', '2023-02-05'),
  (3, 'viewer3@example.com', 'Channel3', '2023-03-10'),
  (4, 'viewer4@example.com', 'Channel4', '2023-04-15'),
  (5, 'viewer5@example.com', 'Channel5', '2023-05-20');

-- Creating CHANNEL_COLLABORATION table
CREATE TABLE CHANNEL_COLLABORATION (
  host_channel_name VARCHAR(255),
  featured_channel_name VARCHAR(255),
  PRIMARY KEY (host_channel_name, featured_channel_name),
  FOREIGN KEY (host_channel_name) REFERENCES CHANNEL(channel_name) ON DELETE CASCADE,
  FOREIGN KEY (featured_channel_name) REFERENCES CHANNEL(channel_name) ON DELETE CASCADE
);

-- Inserting data into CHANNEL_COLLABORATION table
INSERT INTO CHANNEL_COLLABORATION VALUES
  ('Channel1', 'Channel2'),
  ('Channel2', 'Channel3'),
  ('Channel3', 'Channel4'),
  ('Channel4', 'Channel5'),
  ('Channel5', 'Channel1');

-- Creating VIEWER_LIKES_VIDEO_BY_CHANNEL_IN_PLAYLIST table
CREATE TABLE VIEWER_LIKES_VIDEO_BY_CHANNEL_IN_PLAYLIST (
  viewer_email_id VARCHAR(100) REFERENCES VIEWER(email_id) ON DELETE CASCADE,
  channel_name VARCHAR(100) REFERENCES CHANNEL(channel_name) ON DELETE CASCADE,
  video_id VARCHAR(100) REFERENCES VIDEOS(video_id) ON DELETE CASCADE,
  playlist_name VARCHAR(100) REFERENCES PLAYLISTS(name_of_playlist) ON DELETE CASCADE,
  like_date DATE DEFAULT NULL,
  PRIMARY KEY (viewer_email_id, video_id)
);

-- Inserting data into VIEWER_LIKES_VIDEO_BY_CHANNEL_IN_PLAYLIST table
INSERT INTO VIEWER_LIKES_VIDEO_BY_CHANNEL_IN_PLAYLIST VALUES
  ('viewer1@example.com', 'Channel1', 'video1', 'Tech Favorites', '2023-01-05'),
  ('viewer2@example.com', 'Channel2', 'video2', 'Travel Adventures', '2023-02-10'),
  ('viewer3@example.com', 'Channel3', 'video3', 'Cooking Delights', '2023-03-15'),
  ('viewer4@example.com', 'Channel4', 'video4', 'Educational Insights', '2023-04-20'),
  ('viewer5@example.com', 'Channel5', 'video5', 'Language Learning Journey', '2023-05-25');

-- Creating DOB_AGE table
CREATE TABLE DOB_AGE (
  date_of_birth DATE PRIMARY KEY,
  age INT
);

-- Inserting data into DOB_AGE table
INSERT INTO DOB_AGE VALUES
  ('1990-01-15', 32),
  ('1985-05-22', 37),
  ('2000-09-10', 22),
  ('1995-03-03', 28),
  ('1988-11-28', 35);

-- Creating VIEWER_FOLLOWS_PLAYLIST table
CREATE TABLE VIEWER_FOLLOWS_PLAYLIST (
  name_of_playlist VARCHAR(255),
  followed_by VARCHAR(255),
  PRIMARY KEY (name_of_playlist, followed_by),
  FOREIGN KEY (name_of_playlist) REFERENCES PLAYLISTS(name_of_playlist) ON DELETE CASCADE,
  FOREIGN KEY (followed_by) REFERENCES VIEWER(email_id) ON DELETE CASCADE
);

-- Inserting data into VIEWER_FOLLOWS_PLAYLIST table
INSERT INTO VIEWER_FOLLOWS_PLAYLIST VALUES
  ('Tech Favorites', 'viewer1@example.com'),
  ('Travel Adventures', 'viewer2@example.com'),
  ('Cooking Delights', 'viewer3@example.com'),
  ('Educational Insights', 'viewer4@example.com'),
  ('Language Learning Journey', 'viewer5@example.com');

-- Creating CHANNEL_SHORTS table
CREATE TABLE CHANNEL_SHORTS (
  channel_name VARCHAR(255),
  short_id VARCHAR(255),
  PRIMARY KEY (channel_name, short_id),
  FOREIGN KEY (channel_name) REFERENCES CHANNEL(channel_name) ON DELETE CASCADE,
  FOREIGN KEY (short_id) REFERENCES SHORTS(short_id) ON DELETE CASCADE
);

-- Inserting data into CHANNEL_SHORTS table
INSERT INTO CHANNEL_SHORTS VALUES
  ('Channel1', 'short1'),
  ('Channel2', 'short2'),
  ('Channel3', 'short3'),
  ('Channel4', 'short4'),
  ('Channel5', 'short5');

-- Creating CHANNEL_VIDEOS table
CREATE TABLE CHANNEL_VIDEOS (
  channel_name VARCHAR(255),
  video_id VARCHAR(255),
  PRIMARY KEY (channel_name, video_id),
  FOREIGN KEY (channel_name) REFERENCES CHANNEL(channel_name) ON DELETE CASCADE,
  FOREIGN KEY (video_id) REFERENCES VIDEOS(video_id) ON DELETE CASCADE
);

-- Inserting data into CHANNEL_VIDEOS table
INSERT INTO CHANNEL_VIDEOS VALUES
  ('Channel1', 'video1'),
  ('Channel2', 'video2'),
  ('Channel3', 'video3'),
  ('Channel4', 'video4'),
  ('Channel5', 'video5');

-- Creating VIEWER_SUBSCRIBES_TO_CHANNEL table  
CREATE TABLE VIEWER_SUBSCRIBES_TO_CHANNEL (
  viewer_email_id VARCHAR(255),
  channel_name VARCHAR(255),
  PRIMARY KEY (viewer_email_id, channel_name),
  FOREIGN KEY (viewer_email_id) REFERENCES VIEWER(email_id) ON DELETE CASCADE,
  FOREIGN KEY (channel_name) REFERENCES CHANNEL(channel_name) ON DELETE CASCADE
);

-- Inserting data into VIEWER_SUBSCRIBES_TO_CHANNEL table
INSERT INTO VIEWER_SUBSCRIBES_TO_CHANNEL VALUES
  ('viewer1@example.com', 'Channel1'),
  ('viewer2@example.com', 'Channel2'),
  ('viewer3@example.com', 'Channel3'),
  ('viewer4@example.com', 'Channel4'),
  ('viewer5@example.com', 'Channel5');
