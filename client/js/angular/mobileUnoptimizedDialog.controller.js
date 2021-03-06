var BaseCtrl = require('./_base.controller');

MobileUnoptimizedDialogCtrl.prototype = Object.create(BaseCtrl.prototype);
function MobileUnoptimizedDialogCtrl($state, $window, $mdDialog, scheduleFactory) {
  BaseCtrl.call(this, $state, $window, scheduleFactory);

  var vm = this;

  vm.doNotShowMobUnoptDialog = false;
  vm.close = close;

  function close() {
    scheduleFactory.setPreference('showMobUnoptDialog', !vm.doNotShowMobUnoptDialog);
    $mdDialog.hide();
  }
}
angular.module('berkeleyScheduler').controller('MobileUnoptimizedDialogCtrl', [
  '$state',
  '$window',
  '$mdDialog',
  'scheduleFactory',
  MobileUnoptimizedDialogCtrl
]);
