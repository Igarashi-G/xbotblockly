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
 * @author inigo@erlerobot.com (Iñigo Muguruza Goenaga)
 */
'use strict';

goog.provide('Blockly.Python.xbot_sensor');
goog.require('Blockly.Python');

Blockly.Python['xbot_slam_to_pos'] = function(block) {
  var x_pos = block.getFieldValue('MOVE_XPOS');
  var y_pos = block.getFieldValue('MOVE_YPOS');
  var yaw = block.getFieldValue('MOVE_YAW');
  var code = "";
  code += "x_pos = \"" + x_pos.toString() + "\"\n";
  code += "y_pos = \"" + y_pos.toString() + "\"\n";
  code += "yaw = \"" + yaw.toString() + "\"\n";
  code += Blockly.readPythonFile("../blockly/generators/python/scripts/xbot_sensor/xbot_slam_to_pos.py");
  return code;

};
