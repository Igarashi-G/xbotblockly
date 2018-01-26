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

Blockly.Python['xbot_get_laser'] = function(block) {
    var varName = Blockly.Python.valueToCode(block, 'laser', Blockly.Python.ORDER_ATOMIC);
    var code = "";
    code += Blockly.readPythonFile("../blockly/generators/python/scripts/xbot_sensor/xbot_get_lazer.py");
    return code+ varName + " = msg_laser\n"
};


Blockly.Python['xbot_get_imu'] = function(block) {
    var varName = Blockly.Python.valueToCode(block, 'imu', Blockly.Python.ORDER_ATOMIC);
    var code = "";
    code += Blockly.readPythonFile("../blockly/generators/python/scripts/xbot_sensor/xbot_get_imu.py");
    return code+ varName + " = msg_imu\n"
};


Blockly.Python['xbot_get_odom'] = function(block) {
    var varName = Blockly.Python.valueToCode(block, 'odom', Blockly.Python.ORDER_ATOMIC);
    var code = "";
    code += Blockly.readPythonFile("../blockly/generators/python/scripts/xbot_sensor/xbot_get_odom.py");
    return code+ varName + " = msg_odom\n"
};


Blockly.Python['xbot_take_picture'] = function(block) {

    window.open(
        '/pages/images/imageViewer.html',
        '_blank' // <- This is what makes it open in a new window.
    );

    var code = "";
    code += Blockly.readPythonFile("../blockly/generators/python/scripts/xbot_sensor/xbot_take_picture.py");
    return code;

};


Blockly.Python['xbot_take_depth_picture'] = function(block) {

    window.open(
        '/pages/images/imageViewer.html',
        '_blank' // <- This is what makes it open in a new window.
    );

    var code = "";
    code += Blockly.readPythonFile("../blockly/generators/python/scripts/xbot_sensor/xbot_take_depth_picture.py");
    return code;

};


