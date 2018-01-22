/**
 * @license
 *
 * Copyright 2015 Erle Robotics
 * http://erlerobotics.com
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/**
 * @fileoverview Blocks for Erle-Spider.
 * @author victor@erlerobot.com (Víctor Mayoral Vilches)
 * @author ahcorde@erlerobot.com (Alejandro Hernández Cordero)
*/
'use strict';

goog.provide('Blockly.Blocks.xbot_sensor');
goog.require('Blockly.Blocks');


/**
 * Common HSV hue for all blocks in this category.
 */
Blockly.Blocks.brain.HUE = 260;

Blockly.Blocks['xbot_get_laser'] = {
 init: function() {
    this.appendValueInput("laser")
        .appendField("Laser");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setColour(255);
    this.setTooltip('');
    this.setHelpUrl('www.iscas.ac.cn');
  }
};


Blockly.Blocks['xbot_get_imu'] = {
 init: function() {
    this.appendValueInput("imu")
        .appendField("imu");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setColour(255);
    this.setTooltip('read imu data which is a list of distances');//write
    this.setHelpUrl('www.iscas.ac.cn');
  }
};


Blockly.Blocks['xbot_get_odom'] = {
 init: function() {
    this.appendValueInput("odom")
        .appendField("odom");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setColour(255);
    this.setTooltip('');
    this.setHelpUrl('www.iscas.ac.cn');
  }
};


Blockly.Blocks['xbot_take_picture'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Take a picture");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setColour(255);
    this.setTooltip('');
    this.setHelpUrl('www.iscas.ac.cn');
  }
};


Blockly.Blocks['xbot_take_depth_picture'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Take a depth picture");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setColour(255);
    this.setTooltip('');
    this.setHelpUrl('www.iscas.ac.cn');
  }
};
