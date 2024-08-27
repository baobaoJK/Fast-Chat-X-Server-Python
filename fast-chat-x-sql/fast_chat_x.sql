/*
 Navicat Premium Data Transfer

 Source Server         : Localhost
 Source Server Type    : MySQL
 Source Server Version : 50726
 Source Host           : localhost:3306
 Source Schema         : fast_chat_x

 Target Server Type    : MySQL
 Target Server Version : 50726
 File Encoding         : 65001

 Date: 27/08/2024 20:58:15
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for msg_list
-- ----------------------------
DROP TABLE IF EXISTS `msg_list`;
CREATE TABLE `msg_list`  (
  `msg_id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '消息 ID',
  `from_user` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '发送消息的用户',
  `to_user` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT '0' COMMENT '接受消息的用户',
  `msg_content` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '消息内容',
  `msg_date` datetime(0) NULL DEFAULT NULL COMMENT '消息发送时间',
  PRIMARY KEY (`msg_id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 12 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of msg_list
-- ----------------------------
INSERT INTO `msg_list` VALUES (1, '10001', '0', '你好呀！', '2024-08-26 10:00:00');
INSERT INTO `msg_list` VALUES (2, '10002', '0', '你好呀！', '2024-08-26 10:00:00');
INSERT INTO `msg_list` VALUES (9, '10002', '0', '哈哈', '2024-08-27 00:09:54');
INSERT INTO `msg_list` VALUES (8, '10001', '0', '没我可爱', '2024-08-27 00:09:13');
INSERT INTO `msg_list` VALUES (7, '10007', '0', '我可爱吗', '2024-08-27 00:07:55');
INSERT INTO `msg_list` VALUES (6, '10002', '0', '我在写小说', '2024-08-27 00:04:59');
INSERT INTO `msg_list` VALUES (5, '10001', '0', '你在干什么', '2024-08-27 00:04:54');
INSERT INTO `msg_list` VALUES (4, '10002', '0', '今天糟透了！', '2024-08-27 00:03:52');
INSERT INTO `msg_list` VALUES (3, '10001', '0', '今天怎么样？', '2024-08-27 00:03:40');
INSERT INTO `msg_list` VALUES (10, '10007', '0', '睡觉了吗', '2024-08-27 01:06:02');
INSERT INTO `msg_list` VALUES (11, '10001', '0', '还没，还在画画', '2024-08-27 01:06:13');

-- ----------------------------
-- Table structure for user_list
-- ----------------------------
DROP TABLE IF EXISTS `user_list`;
CREATE TABLE `user_list`  (
  `user_id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '用户 ID',
  `user_token` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '用户 Token',
  `user_account` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '用户账号',
  `user_password` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '用户密码',
  `user_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '用户名称',
  `user_phone` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '用户手机号',
  `user_img` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '用户头像',
  `user_status` tinyint(1) UNSIGNED NULL DEFAULT 0 COMMENT '用户状态 1可用 0冻结',
  `create_time` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`user_id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 9 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user_list
-- ----------------------------
INSERT INTO `user_list` VALUES (1, 'd89f3a35931c386956c1a402a8e09941', '10001', '123456', '和泉纱雾', '18500000001', 'user01.jpg', 1, '2024-08-26 00:00:00');
INSERT INTO `user_list` VALUES (2, '9103c8c82514f39d8360c7430c4ee557', '10002', '123456', '和泉政宗', '18500000002', 'user02.jpg', 1, '2024-08-26 00:00:00');
INSERT INTO `user_list` VALUES (3, 'f5dffc111454b227fbcdf36178dfe6ac', '10003', '123456', '古河渚', '18500000003', 'user03.jpg', 1, '2024-08-26 00:00:00');
INSERT INTO `user_list` VALUES (4, 'd783823cc6284b929c2cd8df2167d212', '10004', '123456', '冈崎朋也', '18500000004', 'user04.jpg', 1, '2024-08-26 00:00:00');
INSERT INTO `user_list` VALUES (5, '6eb887126d24e8f1cd8ad5033482c781', '10005', '123456', '小鸟游六花', '18500000005', 'user05.jpg', 1, '2024-08-26 00:00:00');
INSERT INTO `user_list` VALUES (6, '19b1b73d63d4c9ea79f8ca57e9d67095', '10006', '123456', '富樫勇太', '18500000006', 'user06.jpg', 1, '2024-08-26 00:00:00');
INSERT INTO `user_list` VALUES (7, '9cdf26568d166bc6793ef8da5afa0846', '10007', '123456', '可儿那由多', '18500000007', 'user07.jpg', 1, '2024-08-26 00:00:00');
INSERT INTO `user_list` VALUES (8, '670eca4ad5de0e0cfcc60ab3dd008095', '10008', '123456', '羽岛伊月', '18500000008', 'user08.jpg', 1, '2024-08-26 00:00:00');

SET FOREIGN_KEY_CHECKS = 1;
