#include <jni.h>
#include <string>

extern "C" JNIEXPORT jstring JNICALL
Java_com_winlator_core_NativeLib_stringFromJNI(JNIEnv* env, jobject /* this */) {
    return env->NewStringUTF("60FPS_Optimization_Active");
}
