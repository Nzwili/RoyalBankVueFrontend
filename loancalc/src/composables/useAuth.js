import { ref } from "vue";
import { useRouter } from "vue-router";

export function useAuth() {
  const router = useRouter();
  const user = ref(null);

  function loadUser() {
    const stored = localStorage.getItem("user");
    user.value = stored ? JSON.parse(stored) : null;
  }

  function setUser(data) {
    user.value = data;
    localStorage.setItem("user", JSON.stringify(data));
  }

  function logout() {
    localStorage.removeItem("user");
    user.value = null;
    router.push("/login");
  }

  function requireAuth() {
    if (!user.value) {
      router.push("/login");
    }
  }

  return { user, loadUser, setUser, logout, requireAuth };
}
