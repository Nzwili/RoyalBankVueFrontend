<template>
  <div class="blog">
    <!-- Header -->
    <header class="blog-header">
      <h1>Royal Bank Blog</h1>
      <p class="subtitle">Insights, news, and tips from Royal Bank.</p>
    </header>

    <div class="blog-content">
      <!-- Main Section -->
      <section class="posts">
        <!-- Featured Post -->
        <article class="featured-post">
          <h2>💡 How Digital Banking is Changing Finance</h2>
          <p class="meta">Jan 25, 2025 · By Admin</p>
          <p>
            Digital banking has transformed the way customers interact with financial
            institutions. From mobile apps to instant payments, let’s dive into the
            trends redefining banking in 2025.
          </p>
          <a href="#" class="readmore">Read More →</a>
        </article>

        <!-- Blog Cards -->
        <article class="post" v-for="post in posts" :key="post.id">
          <h3>{{ post.title }}</h3>
          <p class="meta">{{ post.date }} · By {{ post.author }}</p>
          <p>{{ post.preview }}</p>
          <div class="tags">
            <span v-for="tag in post.tags" :key="tag" class="tag">#{{ tag }}</span>
          </div>
          <a href="#" class="readmore">Read More →</a>
        </article>
      </section>

      <!-- Sidebar -->
      <aside class="sidebar">
        <div class="widget">
          <h3>Categories</h3>
          <ul>
            <li>Banking Tips</li>
            <li>Loans & Mortgages</li>
            <li>Investments</li>
            <li>Technology</li>
          </ul>
        </div>

        <div class="widget">
          <h3>Recent Posts</h3>
          <ul>
            <li>How to Save More in 2025</li>
            <li>Beginner’s Guide to Investing</li>
            <li>Why Choose Royal Bank?</li>
          </ul>
        </div>
      </aside>
    </div>
  </div>
</template>

<script setup>
const posts = [
  {
    id: 1,
    title: "5 Ways to Save More in 2025",
    date: "Jan 20, 2025",
    author: "Jane Doe",
    preview:
      "Saving money doesn’t have to be hard. These five practical tips will help you grow your savings faster.",
    tags: ["saving", "finance", "tips"],
  },
  {
    id: 2,
    title: "Understanding Mortgages in Simple Terms",
    date: "Jan 18, 2025",
    author: "John Smith",
    preview:
      "Mortgages can be confusing. Here’s a breakdown of the basics every first-time homebuyer should know.",
    tags: ["loans", "mortgage", "guide"],
  },
  {
    id: 3,
    title: "Why Choose Royal Bank?",
    date: "Jan 15, 2025",
    author: "Royal Bank Team",
    preview:
      "From security to customer service, Royal Bank stands out. Here’s why we’re trusted by thousands.",
    tags: ["royalbank", "customers", "trust"],
  },
];
</script>

<style scoped>
.blog {
  padding: 2rem;
  max-width: 1200px;
  margin: auto;
}

.blog-header {
  text-align: center;
  margin-bottom: 2rem;
}

.blog-header h1 {
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
}

.subtitle {
  color: #666;
}

.blog-content {
  display: grid;
  grid-template-columns: 3fr 1fr;
  gap: 2rem;
}

.featured-post {
  background: #f1f9ff;
  padding: 1.5rem;
  border-radius: 10px;
  margin-bottom: 2rem;
  border-left: 5px solid #0077b6;
}

.post {
  background: #fff;
  padding: 1rem;
  border: 1px solid #eee;
  border-radius: 10px;
  margin-bottom: 1.5rem;
  transition: box-shadow 0.2s ease;
}

.post:hover {
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.meta {
  font-size: 0.85rem;
  color: #777;
  margin-bottom: 0.5rem;
}

.readmore {
  display: inline-block;
  margin-top: 0.8rem;
  color: #0077b6;
  text-decoration: none;
  font-weight: 600;
}

.readmore:hover {
  text-decoration: underline;
}

.tags {
  margin-top: 0.5rem;
}

.tag {
  background: #e3f2fd;
  color: #0077b6;
  padding: 0.2rem 0.5rem;
  border-radius: 5px;
  font-size: 0.8rem;
  margin-right: 0.4rem;
}

.sidebar .widget {
  background: #fafafa;
  padding: 1rem;
  border-radius: 8px;
  margin-bottom: 1.5rem;
}

.sidebar h3 {
  margin-bottom: 0.8rem;
}

.sidebar ul {
  list-style: none;
  padding: 0;
}

.sidebar li {
  margin-bottom: 0.6rem;
  color: #0077b6;
  cursor: pointer;
}
</style>
