function enumMethods(targetClass)
{
	var ownMethods = ObjC.classes[targetClass].$ownMethods;

	return ownMethods;
}

function hierarchy() {
  var objc_copyClassNamesForImage = new NativeFunction(Module.findExportByName(
    null, 'objc_copyClassNamesForImage'), 'pointer', ['pointer', 'pointer'])
  var free = new NativeFunction(Module.findExportByName(null, 'free'), 'void', ['pointer'])
  var classes = new Array(count)
  var p = Memory.alloc(Process.pointerSize)
  Memory.writeUInt(p, 0)
  var path = ObjC.classes.NSBundle.mainBundle().executablePath().UTF8String()
  var pPath = Memory.allocUtf8String(path)
  var pClasses = objc_copyClassNamesForImage(pPath, p)
  var count = Memory.readUInt(p)
  for (var i = 0; i < count; i++) {
    var pClassName = Memory.readPointer(pClasses.add(i * Process.pointerSize))
    classes[i] = Memory.readUtf8String(pClassName)
  }
  free(pClasses)

  var tree = {}
  for (var aClass in ObjC.classes) {
	if (ObjC.classes.hasOwnProperty(aClass)) {
		var clazz = ObjC.classes[aClass]
		var chain = [aClass, ObjC.classes[aClass].$ownMethods]
		while (clazz = clazz.$superClass) {
		  chain.unshift(clazz.$className)
		}
		var node = tree
		chain.forEach(function(clazz) {
		node[clazz] = node[clazz] || {}
		node = node[clazz]
		})
	} 
  }
  return tree
}

console.log(JSON.stringify(hierarchy(),null,2));
